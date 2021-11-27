#!/bin/sh
make lro M=03
make lro M=04
make lro M=06
make lro M=08
make lre M=03
make lre M=04
make lre M=06
make lre M=08
make lre M=12
make sro M=03 SEED=01
make sro M=03 SEED=02
make sro M=03 SEED=03
make sro M=04 SEED=01
make sro M=04 SEED=02
make sro M=04 SEED=03
make sro M=06 SEED=01
make sro M=06 SEED=02
make sro M=06 SEED=03
make sro M=08 SEED=01
make sro M=08 SEED=02
make sro M=08 SEED=03
make sre M=03 SEED=01
make sre M=03 SEED=02
make sre M=03 SEED=03
make sre M=04 SEED=01
make sre M=04 SEED=02
make sre M=04 SEED=03
make sre M=06 SEED=01
make sre M=06 SEED=02
make sre M=06 SEED=03
make sre M=08 SEED=01
make sre M=08 SEED=02
make sre M=08 SEED=03
make sre M=12 SEED=01
make sre M=12 SEED=02
make sre M=12 SEED=03
make data
