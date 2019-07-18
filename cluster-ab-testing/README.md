# AB-testing by clusters
Speaker: [Bertil Hatt](https://github.com/bertilhatt) and [João Martins](https://pydata.org/london2019/speaker/profile/136/)

## Description

We all know and love AB-testing, especially organisations with a large number of users. What happens when you want to test your idea either on a small sample? Say to test an over-the-line (OTL) ad campaign in different cities, or on partners, or on your customer support team that has “only” hundreds of member? AB-test by cluster, simulate the sensitivity of your test—and impress your stakeholders!

## Abstract

### AB-test, all the time

Any organisation who monitors their activity in detail should run AB-tests, aka Random control trial (RCT) for every change that they are considering. Trying to correct for confounding parameters is incredibly hard. A well-calibrated AB-test allows you to control the risk of exposing users to an inferior experience. Most tech companies and health companies do, especially when they have a large number of users.

What happens when you want to test your idea but you can’t expose individuals independently? For instance, if you are trying an over-the-line ad campaign on the side of buses and at bus stops, you can’t expose one customer without exposing their neighbour. If you are testing different price policies, you risk outrage or opportunistic behaviours unless you test, say, per country.

### Platforms

This problem is frequent for marketplaces, two- or three-sided markets, platforms who have different types of users. On one side, users are typically are numerous enough to be tested with a standard AB-testing protocol. But in many other contexts, there might not be enough flexibility, or enough users, to pick a clean A and B split that is reassuringly large.

One common suggestion is to pick equivalent users and pair them two-by-two. That solution can be very limiting: how to define “equivalent”? How close is close enough? Should we exclude users without an obvious equivalent? Does it actually make the test better?

Another common situation is when trying to improve your customer support practices; that team can have dozens or even hundreds of members, but rarely many thousands. Can you test on such a small sample and still control for with various experience levels, cultural context?

### Source code

Based on the experience working for four different platforms, we will present a token code base. That code will let you, take your data (or our randomly generated data sets) through a process to split two or more segments, aggregate and to test that sample. We’ll explain the role of simulations: AA-test and Sensitivity analysis. Such an effort before any test allows you to set expectations. When dealing with either a small data-sets or circumstances with clustered constraint, you can let your stakeholders know what to expect from a test.

We will also investigate processes that have been suggested improve the split: remove outliers, iteratively find a good split, and check it those improve the quality of the test. Finally, we’ll investigate whether you can run several simultaneous tests on the same small sample.

### Interactive talk

The codebase is available today as a notebook on Github today. The code documents every step; requirements are basic PyData libraries, so you can understand each step and check if any conclusion holds for smaller or larger samples; or if other constraints change the precision and sensitivity of the test.

The talk is full of… ::cough:: possible improvements and opportunities for debate. We encourage you to look at the content now, make suggestions, submit changes, send merge requests. During the conversation, we‘ll try to go through the bulk of the process but there will be several large sections for questions throughout, to make sure you can help us all improve.
