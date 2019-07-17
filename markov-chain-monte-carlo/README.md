# An Introduction to Markov chain Monte Carlo using PyMC3
Speaker: [Chris Fonnesbeck](https://github.com/fonnesbeck)

## Description

Markov chain Monte Carlo (MCMC) is the most common approach for performing Bayesian data analysis. MCMC is a general class of algorithms that uses simulation to estimate a variety of statistical models. This tutorial will introduce users how to use MCMC for fitting statistical models using PyMC3, a Python package for probabilistic programming.

## Abstract

Bayesian methods are powerful tools for data science applications, complimenting traditional statistical and machine learning methods. Importantly, Bayesian models generate predictions and inferences that fully account for uncertainty. The main tool for conducting Bayesian analysis is Markov chain Monte Carlo (MCMC), a computationally-intensive numerical approach that allows a wide variety of models to be estimated. MCMC algorithms are available in several Python libraries, including PyMC3. I will teach users a practical, effective workflow for applying Bayesian statistics using MCMC via PyMC3 using real-world examples.

This tutorial is intended for analysts, data scientists and machine learning practitioners. Anyone looking for effective ways of making predictions and obtaining inference from datasets should find it useful. The material will assume an intermediate level of Python familiarity. Ideally, attendees should be familiar with Numpy and Jupyter. There is no expectation of students having a statistical background. Having completed the tutorial, students should be able to build basic Bayesian statistical models using their own data, validate those models, and interpret their output.

## Introduction to PyMC3

    Gentle introduction to the PyMC3 API using a real example
    What is a Bayesian model?
        Running example: comparison of one group with a continuous outcome to a threshold value
    How do we make a model Bayesian? - Mapping a model onto Bayes' formula
    Overview of the PyMC3 API
        The PyMC3 Model
        Probability distributions
        Adding data to the model
        Estimating the values of the variables
    Three steps of the Bayesian workflow

## Coding Bayesian Models

    Challenge: how do we encode a Bayesian statistical model in PyMC3?
    This chapter will focus on Step 1 of the workflow
    Employ a slightly more sophisticated model: comparing 2 groups with continuous outcomes
        Approach: start with original model, and see what needs to be changed in order to accomodate 2 groups
    How do we translate equations into code?
        Relate each model component to Bayes' formula
    Picking your priors
        Stochastic objects
    Transforming variables
        Determinsitic objects
    Adding data via the likelihood function
        Stochastic objects with observed values

## Fitting Models with MCMC

    Challenge: how do we fit our PyMC3 model to our dataset?
    Why do we need MCMC?
        Using simulation when problems cannot be solved analytically
    Overview of the Metropolis algorithm
        Coding a simple MCMC algorithm by hand
            Initializing variables
            Proposing values for variables
            Accepting or rejecting proposed values
            Obtaining an estimate from the simulated values
    MCMC algorithms in PyMC3
        Gradient-based MCMC
        Using the sample function to fit your model

## Checking your Model

    Challenge: how do we know if our model is any good, and what can we do if it isn't?
    How many samples do you need?
    Using convergence diagnostics to see if you're done
    What to do about autocorrelation
    Checking the fit of your model
    Reparameterizing your model to improve model performance

## Summarizing and Interpreting Model Output

    Challenge: how do we obtain useful output from our model, such as predictions, estimates and plots?
    Extracting samples from the model trace
    Summarizing and exporting model output
    How to interpret what you have done
    Producing meaningful graphics
    Communicating your results to others
