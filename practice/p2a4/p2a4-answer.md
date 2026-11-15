# Q

Practice this question: two versions of a code-review agent each review the same 20 pull requests, and one succeeds on 16 while the other succeeds on 14. Is the first one better? Cover task coverage, paired outcomes, repeated runs, quality, cost, and time.

# A

"Better" must be defined - on which tasks, at what cost, what level of quality, how long it takes.

We would want to know:
- were the tasks tested representative of the work the agents need to be used on?
- task importance: for each task tested, how critical or important is it that the agent succeeds?
- task type distribution: and what is the distribution of the types of tasks in practice? even a less important task becomes important if it represents 90% of the work.
- on which tasks did the agents differ? these are the ones to focus on. how important were they, how often do they need to be done? what's the cost of failure? why did an agent fail on it vs succeed?
- was the sample size representative? ensure enough tests were run. perform repeated runs of the same test also to see if it is consistent.
- compare cost in terms of tokens, human input/behavior needed
- compare time spent for each agent per task
- also grade quality of work, as one agent may perform signficantly better even though both pass (or fail).
