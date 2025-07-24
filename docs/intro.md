(intro)=

```{todo}
This book is still written and currently an early draft.
```

# Fesslix – Stochastic Analysis

## What is Fesslix?

**Fesslix** is a Python module for stochastic analysis.

The name *Fesslix* is an acronym for **F**ramework for **E**ngineering **S**tochastic **S**imulation using
**L**ikelihood-based methods and **I**nference under **X**-uncertainty.

```{note}
Fesslix is currently being rewritten as a Python module. 
Originally Fesslix was a standalone C++ application that parsed/processed parameter files - which is, in this context, referred to as *Fesslix-Legacy*.

All features available in *Fesslix-Legacy* are also available in the Python module of Fesslix - if you use the internal scripting language of Fesslix.
However, only a fraction of the available features is currently exposed/documented in the Python interface.

For a documentation of *Fesslix-Legacy*, please have a look at the [documentation of Fesslix-Legacy](http://download.fesslix.org/Fesslix_User_Guide_Legacy.pdf) and the [website of Fesslix-Legacy](http://legacy.fesslix.org).

Important features of *Fesslix-Legacy* that are currently not exposed in the Python module of Fesslix are:
- Perform non-intrusive reliability analysis or Bayesian updating either
  - by expressing problems directly in Fesslix
  - by means of an Octave/Matlab interface
  - by means of a Python interface
  - by linking external applications/libraries to Fesslix
    - through a C++ or Fortran interface
    - through running commands on the command line
- Flexible input language for writing Fesslix parameter files
  - control flow statements (e.g. if, for, while)
  - most parameters can be defined as functions
- Extensible by means of modules
  - examples of modules available by default:
    - **Linear finite element analysis using truss, beam and plane stress/strain elements**
    - Bayesian networks
    - Working with response surfaces
    - **Spectral Stochastic Finite Elements**
```

## Legacy Fesslix




## Table of Contents

```{tableofcontents}
```


