#!/usr/bin/python

#####################################################################################
# Copyright (c) 2021 Marijn Heule, Randal E. Bryant, Carnegie Mellon University
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
########################################################################################


import datetime
import sys

# Resolution engine tailored to generating proofs 
# having a "V" structure, consisting of two linear chains merging together

# Special value to represent true/tautology
# It's negation represents false/invalid
tautologyId = 1000 * 1000 * 1000

# Clean up clause.
# Remove duplicates + false
# Detect when tautology
# Make sure that literal with highest-numbered variable stays at front
# (by sorting in reverse order of literal number)
def cleanClause(literalList):
    slist = sorted(literalList, key = lambda v: -abs(v))
    while len(slist) > 0:
        # Tautology and Null will be in front
        first = slist[0]
        if abs(first) != tautologyId:
            break
        elif first == tautologyId:
            return tautologyId
        else:
            slist = slist[1:]
    if len(slist) == 0:
        return -tautologyId
    elif len(slist) == 1:
        return slist
    else:
        nlist = [slist[0]]
        for i in range(1, len(slist)):
            if slist[i-1] == slist[i]:
                continue
            if slist[i-1] == -slist[i]:
                return tautologyId
            nlist.append(slist[i])
        return nlist

def regularClause(clause):
    return clause is not None and clause != tautologyId and clause != -tautologyId

def showClause(clause):
    if clause is None:
        return "NONE"
    if clause == tautologyId:
        return "TAUT"
    elif clause == -tautologyId:
        return "NIL"
    return str(clause)

class ResolveException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Resolve Exception: " + str(self.value)

# Given two clauses, each processed by cleanClause,
# attempt to resolve them.
# Return result if successful, or None if fails
def resolveClauses(clause1, clause2):
    if not regularClause(clause1):
        msg = "Cannot do resolution on clause %s" % showClause(clause1)
        raise ResolveException(msg)
    if not regularClause(clause2):
        msg = "Cannot do resolution on clause %s" % showClause(clause2)
        raise ResolveException(msg)
    result = []
    resolutionVariable = None
    while True:
        if len(clause1) == 0:
            if resolutionVariable is None:
                result = None
            else:
                result += clause2
            break
        if len(clause2) == 0:
            if resolutionVariable is None:
                result = None
            else:
                result += clause1
            break
        l1 = clause1[0]
        l2 = clause2[0]
        rc1 = clause1[1:]
        rc2 = clause2[1:]
        if abs(l1) == abs(l2):
            clause1 = rc1
            clause2 = rc2
            if l1 == l2:
                result.append(l1)
            else:
                if resolutionVariable is None:
                    resolutionVariable = abs(l1)
                else:
                    return None # Multiple complementary literals
        elif abs(l1) > abs(l2):
            clause1 = rc1
            result.append(l1)
        else:
            clause2 = rc2
            result.append(l2)
    return result

def testClauseEquality(clause1, clause2):
    if clause1 is None or clause2 is None:
        return False
    if not regularClause(clause1):
        return clause1 == clause2
    if not regularClause(clause2):
        return False
    while True:
        if len(clause1) == 0:
            return len(clause2) == 0
        elif len(clause2) == 0:
            return False
        else:
            l1 = clause1[0]
            l2 = clause2[0]
            clause1 = clause1[1:]
            clause2 = clause2[1:]
            if l1 != l2:
                return False

def testClauseSubset(clause1, clause2):
    if clause1 is None or clause2 is None:
        return False
    if not regularClause(clause1):
        return clause1 == clause2
    if not regularClause(clause2):
        return False
    idx1 = 0
    idx2 = 0
    while idx1 < len(clause1):
        if idx2 >= len(clause2):
            return False
        head1 = clause1[idx1]
        head2 = clause2[idx2]
        if abs(head1) > abs(head2):
            return False
        elif head1 == head2:
            idx1 += 1
            idx2 += 1
        elif abs(head1) < abs(head2):
            idx2 += 1
    return True
            

# Given ordered list of clauses (indicated by clause IDs), attempt resolution on each successive one.
# clauseDict is mapping from clause ID to literal list
# Return resulting clause + list of clauses used during resolution in reverse order
def chainResolve(clauseList, clauseDict):
    resolved = False
    if len(clauseList) == 0:
        raise ResolveException("Cannot do chain resolution on empty list of clauses")
    id = clauseList[0]
    antecedents = [id]
    result = clauseDict[id]
    for id in clauseList[1:]:
        clause = clauseDict[id]
        nresult = resolveClauses(result, clause)
        if nresult is not None:
            antecedents.append(id)
            result = nresult
            resolved = True
    antecedents.reverse()
    return (result, antecedents) if resolved else None


# Record information about resolutions
# Build signature consisting of rule names of clauses generated
# Also histogram of number of clauses generated by each call
# by multiChainResolve
class Profiler:
    remap = {"ANDH" : "ANDx", "IMH" : "IMx",
             "VHD"  : "VxD", "VHU" : "VxU",
             "UHD"  : "UxD", "UHU" : "UxU",
             "WHD"  : "WxD", "WHU" : "WxU",
             "ANDL" : "ANDx", "IML" : "IMx",
             "VLD"  : "VxD", "VLU" : "VxU",
             "ULD"  : "UxD", "ULU" : "UxU",             
             "WLD"  : "WxD", "WLU" : "WxU"}

    prover = None
    prefix = "CHAIN"
    signatureDict = {}

    def __init__(self, prover):
        self.prover = prover
        self.signatureDict = {}

    def profile(self, chain, pair, ruleIndex):
        if self.prover.verbLevel <= 1:
            return
        cnames = []
        for k in ruleIndex.keys():
            if ruleIndex[k] in chain and self.remap[k] not in cnames:
                cnames.append(self.remap[k])
        cnames.sort()
        sigc = '+'.join(cnames)
        a = pair[1]
        # Find names of clauses used in antecedent list a
        anames = []
        for k in ruleIndex.keys():
            if ruleIndex[k] in a and self.remap[k] not in anames:
                anames.append(self.remap[k])
        anames.sort()
        siga = '+'.join(anames)
        sig = sigc + " " + siga
        if sig in self.signatureDict:
            self.signatureDict[sig] += 1
        else:
            self.signatureDict[sig] = 1

    def summarize(self):
        if self.prover.verbLevel <= 1:
            return
        total = sum(self.signatureDict.values())
        self.prover.writer.write("Chain resolution signatures:\n")
        sigList = sorted(self.signatureDict.keys())
        for sig in sigList:
            count = self.signatureDict[sig]
            self.prover.writer.write("%s %s %d\n" % (self.prefix, sig, count))        
        
    

class VResolver:
    prover = None
    rule1Names = []
    rule2Names = []
    antecedentCount = 0
    clauseCount = 0
    runCount = 0
    tryCount = 0
    profiler = None
    # Should we just enumerate last few possibilities, 
    # or try to fully determine how to perform handle each chain?
    # 2020-09-14: Must enumerate to ensure testing for shorter proofs
    enumerate = True
    
    def __init__(self, prover, rule1Names, rule2Names):
        self.prover = prover
        self.rule1Names = rule1Names
        self.rule2Names = rule2Names
        self.antecedentCount = 0
        self.clauseCount = 0
        self.runCount = 0
        self.tryCount = 0
        self.profiler = Profiler(prover)

    def showRules(self, ruleIndex):
        rlist = ["%s:%d" % (k, ruleIndex[k]) for k in ruleIndex.keys() if ruleIndex[k] != tautologyId]
        return "[" + ", ".join(rlist) + "]"

    def run(self, targetClause, ruleIndex, comment):
        self.cleanIndex(ruleIndex)
        if self.enumerate:
            return self.runSet(targetClause, ruleIndex, comment)
        else:
            return self.runSingle(targetClause, ruleIndex, comment)

    def cleanIndex(self, ruleIndex):
        for k in list(ruleIndex.keys()):
            if ruleIndex[k] == tautologyId:
                del ruleIndex[k]

    def runSingle(self, targetClause, ruleIndex, comment):
        self.runCount += 1
        pair1 = self.buildChain(self.rule1Names, ruleIndex)
        pair2 = self.buildChain(self.rule2Names, ruleIndex)
        (r1, a1) = pair1
        (r2, a2) = pair2
        r = resolveClauses(r1, r2)
        self.tryCount += 1
        if r is None:
            msg = "Could not justify clause %s.  Could not resolve r1 = %s and r2 = %s)" % (showClause(targetClause), showClause(r1), showClause(r2))
            raise ResolveException(msg)
        if not testClauseSubset(r, targetClause):
            msg = "Could not justify clause %s.  Got resolvent %s from r1 = %s and r2 = %s)" % (showClause(targetClause), showClause(r), showClause(r1), showClause(r2))
            raise ResolveException(msg)

        return self.generateProof(r, r1, a1, r2, a2, comment)

    def runSet(self, targetClause, ruleIndex, comment):
        self.runCount += 1
        pairList1 = self.buildChainSet(self.rule1Names, ruleIndex)
        pairList2 = self.buildChainSet(self.rule2Names, ruleIndex)
        for pair1 in pairList1:
            (r1, a1) = pair1
            for pair2 in pairList2:
                (r2, a2) = pair2
                r = resolveClauses(r1, r2)
                self.tryCount += 1
                if r is not None and testClauseSubset(r, targetClause):
                    return self.generateProof(r, r1, a1, r2, a2, comment)
        if self.prover.verbLevel >= 3:
            if comment is not None:
                print("Failing: " + comment)
            print("Trying to generate target clause %s" % showClause(targetClause))
            print("%d candidate clauses:" % len(ruleIndex))
            for k in ruleIndex.keys():
                v = ruleIndex[k]
                print("%s: %s: %s" % (str(k), str(v), showClause(self.prover.clauseDict[v])))
        msg = "Could not justify clause %s.  Tried %d combinations" % (showClause(targetClause), len(pairList1) * len(pairList2))
        raise ResolveException(msg)


    # Filter set of clauses to include only those useful in single-clause resolution proof
    # This version will be overloaded by operation-specific ones
    def filterClauses(self, idList, ruleIndex):
        return idList[0]

    # Build chain of clauses for resolution proof
    def buildChain(self, ruleNames, ruleIndex):
        clauseDict = self.prover.clauseDict
        chain = []
        for n in ruleNames:
            if n in ruleIndex:
                chain.append(ruleIndex[n])
        if len(chain) == 0:
            msg = "No applicable rules in chain (rule index = %s)." % (self.showRules(ruleIndex))
            raise ResolveException(msg)
        if len(chain) == 1:
            id = chain[0]
            pair = (clauseDict[id], [id])
        else:
            pair = chainResolve(chain, clauseDict)
            if pair is None:
                id = self.filterClauses(chain, ruleIndex)
                pair = (clauseDict[id], [id])
        self.profiler.profile(chain, pair, ruleIndex)
        return pair

    # Build chain of clauses for resolution proof
    def buildChainSet(self, ruleNames, ruleIndex):
        clauseDict = self.prover.clauseDict
        chain = []
        firstRule = False
        checkFirst = True
        for n in ruleNames:
            if n in ruleIndex:
                gotRule = False
                if ruleIndex[n] != tautologyId:
                    gotRule = True
                    chain.append(ruleIndex[n])
                if checkFirst:
                    firstRule = gotRule
                    checkFirst = False
        if len(chain) == 0:
            msg = "No applicable rules in chain (rule index = %s)." % (self.showRules(ruleIndex))
            raise ResolveException(msg)
        if len(chain) == 1:
            id = chain[0]
            pairList = [(clauseDict[id], [id])]
        else:
            pair = chainResolve(chain, clauseDict)
            if pair is None:
                pairList = [(clauseDict[id], [id]) for id in chain]
            elif firstRule:
                pairList = [pair]
            else:
                # Return source clauses so that resolver can look for shorter chains
                pairList = [(clauseDict[id], [id]) for id in chain] + [pair]
        return pairList

    
    def generateProof(self, r, r1, a1, r2, a2, comment):
        self.antecedentCount += len(a1) + len(a2)
        self.prover.proofCount += 1
        self.clauseCount += 1
        if len(a1) == 1:
            id = self.prover.createClause(r, a1 + a2, comment, isInput = False)
            return id, [id]
        elif len(a2) == 1:
            id = self.prover.createClause(r, a2 + a1, comment, isInput = False)
            return id, [id]
        else:
            id1 = self.prover.createClause(r1, a1, comment, isInput = False)
            id = self.prover.createClause(r, [id1] + a2, comment = None, isInput = False)
            self.prover.proofCount += 1
            self.clauseCount += 1
            return id, [id1, id]


    def summarize(self):
        if self.prover.verbLevel >= 1 and self.runCount > 0:
            antecedentAvg = float(self.antecedentCount) / float(self.runCount)
            clauseAvg = float(self.clauseCount) / float(self.runCount)
            tryAvg = float(self.tryCount) / float(self.runCount)
            self.prover.writer.write("  Avg antecedents / proof = %.2f.  Avg clauses / proof = %.2f.  Avg tries / proof = %.2f\n" % (antecedentAvg, clauseAvg, tryAvg))
            self.profiler.summarize()


class AndResolver(VResolver):

    def __init__(self, prover):
        rule1Names = ["ANDH", "WHU", "UHD", "VHD"]
        rule2Names = ["ANDL", "WLU", "ULD", "VLD"]
        VResolver.__init__(self, prover, rule1Names, rule2Names)
        self.profiler.prefix = "ANDCHAIN"

    # Filter set of clauses to include only the one useful in single-clause resolution proof
    # Guaranteed that have at least on clause
    def filterClauses(self, idList, ruleIndex):
        # See if WHU or WLU is in list
        if "WHU" in ruleIndex:
            wid = ruleIndex["WHU"]
            id = idList[0]
            if id == wid:
                return id
        if "WLU" in ruleIndex:
            wid = ruleIndex["WLU"]
            id = idList[0]
            if id == wid:
                return id

        clauseDict = self.prover.clauseDict

        if "UHD" in ruleIndex and "VHD" in ruleIndex:
            uid = ruleIndex["UHD"]
            vid = ruleIndex["VHD"]
            if uid == idList[0] and vid == idList[1]:
                uclause = clauseDict[uid]
                vclause = clauseDict[vid]
                if len(uclause) < len(vclause):
                    return uid
                else:
                    return vid
        if "ULD" in ruleIndex and "VLD" in ruleIndex:
            uid = ruleIndex["ULD"]
            vid = ruleIndex["VLD"]
            if uid == idList[0] and vid == idList[1]:
                uclause = clauseDict[uid]
                vclause = clauseDict[vid]
                if len(uclause) < len(vclause):
                    return uid
                else:
                    return vid

        msg = "No applicable rules in chain (idList = %s, rule index = %s)." % (str(idList), self.showRules(ruleIndex))
        raise ResolveException(msg)

            


class ImplyResolver(VResolver):

    def __init__(self, prover):
        rule1Names = ["IMH", "UHD", "VHU"]
        rule2Names = ["IML", "ULD", "VLU"]
        VResolver.__init__(self, prover, rule1Names, rule2Names)
        self.profiler.prefix = "IMPLYCHAIN"

    # Filter set of clauses to include only those useful in single-clause resolution proof
    def filterClauses(self, idList, ruleIndex):
        clauseDict = self.prover.clauseDict
        if "UHD" in ruleIndex and "VHU" in ruleIndex:
            uid = ruleIndex["UHD"]
            vid = ruleIndex["VHU"]
            if uid == idList[0] and vid == idList[1]:
                uclause = clauseDict[uid]
                vclause = clauseDict[vid]
                if len(uclause) < len(vclause):
                    return uid
                else:
                    return vid
        if "ULD" in ruleIndex and "VLU" in ruleIndex:
            uid = ruleIndex["ULD"]
            vid = ruleIndex["VLU"]
            if uid == idList[0] and vid == idList[1]:
                uclause = clauseDict[uid]
                vclause = clauseDict[vid]
                if len(uclause) < len(vclause):
                    return uid
                else:
                    return vid

        msg = "No applicable rules in chain (rule index = %s)." % (self.showRules(ruleIndex))
        raise ResolveException(msg)

        
