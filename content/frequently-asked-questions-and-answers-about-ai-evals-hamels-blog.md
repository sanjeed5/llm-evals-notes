---
title: "Frequently Asked Questions (And Answers) About AI Evals \u2013 Hamel\u2019\
  s Blog"
source_url: https://hamel.dev/blog/posts/evals-faq/
source_domain: hamel.dev
date_fetched: '2025-08-08T06:31:17.407972+00:00'
hash: 0ced771feff396e9626521ea46d7f3ca28ae3f44870b6853267acd173d394e4c
---

## Stay Ahead in AI Evals

Found this useful? The newsletter goes deeper with practical frameworks, case studies and analysis for building AI you can trust.

Keep Me Updated

We won't send you spam. Unsubscribe at any time.

This document curates the most common questions Shreya and I received while [teaching](https://bit.ly/evals-ai) 700+ engineers & PMs AI Evals. _Warning: These are sharp opinions about what works in most cases. They are not universal truths. Use your judgment._

* * *

**👉 _If you want to learn more about AI Evals, check out our [AI Evals course](https://bit.ly/evals-ai)_**. Here is a [35% discount code](https://bit.ly/evals-ai) for readers. 👈

* * *

# Listen to the audio version of this FAQ

If you prefer to listen to the audio version (narrated by AI), you can play it [here](https://soundcloud.com/hamel-husain/llm-evals-faq).

SoundCloud Widget

[Hamel Husain](https://soundcloud.com/hamel-husain "Hamel Husain") · [LLM Evals FAQ](https://soundcloud.com/hamel-husain/llm-evals-faq "LLM Evals FAQ")

# Getting Started & Fundamentals

## Q: What are LLM Evals? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-are-llm-evals)

If you are completely new to product-specific LLM evals (not foundation model benchmarks), see these posts: [part 1](https://hamel.dev/blog/posts/evals/), [part 2](https://hamel.dev/blog/posts/llm-judge/) and [part 3](https://hamel.dev/blog/posts/field-guide/). Otherwise, keep reading.

[![](https://hamel.dev/blog/posts/evals/images/diagram-cover.png)](https://hamel.dev/evals)

[**Your AI Product Needs Eval (Evaluation Systems)**](https://hamel.dev/evals)

**Contents:**

1. Motivation
2. Iterating Quickly == Success

3. Case Study: Lucy, A Real Estate AI Assistant
4. The Types Of Evaluation
1. Level 1: Unit Tests
2. Level 2: Human & Model Eval
3. Level 3: A/B Testing
4. Evaluating RAG
5. Eval Systems Unlock Superpowers For Free
1. Fine-Tuning
2. Data Synthesis & Curation
3. Debugging

[![](https://hamel.dev/blog/posts/llm-judge/images/cover_img.png)](https://hamel.dev/llm-judge/)

[**Creating a LLM-as-a-Judge That Drives Business Results**](https://hamel.dev/llm-judge/)

**Contents:**

01. The Problem: AI Teams Are Drowning in Data
02. Step 1: Find The Principal Domain Expert
03. Step 2: Create a Dataset
04. Step 3: Direct The Domain Expert to Make Pass/Fail Judgments with Critiques
05. Step 4: Fix Errors
06. Step 5: Build Your LLM as A Judge, Iteratively
07. Step 6: Perform Error Analysis
08. Step 7: Create More Specialized LLM Judges (if needed)
09. Recap of Critique Shadowing
10. Resources

[![](https://hamel.dev/blog/posts/field-guide/images/field_guide_2.png)](https://hamel.dev/field-guide)

[**A Field Guide to Rapidly Improving AI Products**](https://hamel.dev/field-guide)

**Contents:**

1. How error analysis consistently reveals the highest-ROI improvements
2. Why a simple data viewer is your most important AI investment
3. How to empower domain experts (not just engineers) to improve your AI
4. Why synthetic data is more effective than you think
5. How to maintain trust in your evaluation system
6. Why your AI roadmap should count experiments, not features

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-are-llm-evals.html)

## Q: What is a trace? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-is-a-trace)

A trace is the complete record of all actions, messages, tool calls, and data retrievals from a single initial user query through to the final response. It includes every step across all agents, tools, and system components in a session: multiple user messages, assistant responses, retrieved documents, and intermediate tool interactions.

**Note on terminology:** Different observability vendors use varying definitions of traces and spans. [Alex Strick van Linschoten’s analysis](https://mlops.systems/posts/2025-06-04-instrumenting-an-agentic-app-with-arize-phoenix-and-litellm.html#llm-tracing-tools-naming-conventions-june-2025) highlights these differences (screenshot below):

![](https://hamel.dev/blog/posts/evals-faq/alex.jpeg)

Vendor differences in trace definitions as of 2025-07-02

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-is-a-trace.html)

## Q: What’s a minimum viable evaluation setup? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-whats-a-minimum-viable-evaluation-setup)

Start with [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed), not infrastructure. Spend 30 minutes manually reviewing 20-50 LLM outputs whenever you make significant changes. Use one [domain expert](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs) who understands your users as your quality decision maker (a “ [benevolent dictator](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs)”).

If possible, **use notebooks** to help you review traces and analyze data. In our opinion, this is the single most effective tool for evals because you can write arbitrary code, visualize data, and iterate quickly. You can even build your own [custom annotation interface](https://hamel.dev/blog/posts/evals-faq/#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs) right inside notebooks, as shown in this [video](https://youtu.be/aqKUwPKBkB0?si=5KDmMQnRzO_Ce9xH).

Build Your Own Eval Tools With Notebooks! - YouTube

[Photo image of Hamel Husain](https://www.youtube.com/channel/UC__dUuqF5w4OnbW221JxmKg?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Hamel Husain

11.1K subscribers

[Build Your Own Eval Tools With Notebooks!](https://www.youtube.com/watch?v=aqKUwPKBkB0)

Hamel Husain

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/whats-a-minimum-viable-evaluation-setup.html)

## Q: How much of my development budget should I allocate to evals? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-much-of-my-development-budget-should-i-allocate-to-evals)

It’s important to recognize that evaluation is part of the development process rather than a distinct line item, similar to how debugging is part of software development.

You should always be doing [error analysis](https://www.youtube.com/watch?v=qH1dZ8JLLdU). When you discover issues through error analysis, many will be straightforward bugs you’ll fix immediately. These fixes don’t require separate evaluation infrastructure as they’re just part of development.

The decision to build automated evaluators comes down to [cost-benefit analysis](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-automated-evaluators-for-every-failure-mode-i-find). If you can catch an error with a simple assertion or regex check, the cost is minimal and probably worth it. But if you need to align an LLM-as-judge evaluator, consider whether the failure mode warrants that investment.

In the projects we’ve worked on, **we’ve spent 60-80% of our development time on error analysis and evaluation**. Expect most of your effort to go toward understanding failures (i.e. looking at data) rather than building automated checks.

Be [wary of optimizing for high eval pass rates](https://ai-execs.com/2_intro.html#a-case-study-in-misleading-ai-advice). If you’re passing 100% of your evals, you’re likely not challenging your system enough. A 70% pass rate might indicate a more meaningful evaluation that’s actually stress-testing your application. Focus on evals that help you catch real issues, not ones that make your metrics look good.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-much-of-my-development-budget-should-i-allocate-to-evals.html)

## Q: Will today’s evaluation methods still be relevant in 5-10 years given how fast AI is changing? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-will-todays-evaluation-methods-still-be-relevant-in-5-10-years-given-how-fast-ai-is-changing)

Yes. Even with perfect models, you still need to verify they’re solving the right problem. The need for systematic [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed), domain-specific testing, and monitoring will still be important.

Today’s prompt engineering tricks might become obsolete, but you’ll still need to understand failure modes. Additionally, a LLM cannot read your mind, and [research shows](https://arxiv.org/abs/2404.12272) that people need to observe the LLM’s behavior in order to properly externalize their requirements.

For deeper perspective on this debate, see these two viewpoints: [“The model is the product”](https://m.youtube.com/watch?si=qknrtQeITqJ7VsJH&v=4dUFIRj-BWo&feature=youtu.be) versus [“The model is NOT the product”](https://www.youtube.com/watch?v=EEw2PpL-_NM).

**“The model is the product”:**

The Model is the Product - YouTube

[Photo image of Data Council](https://www.youtube.com/channel/UCAezwIIm1SfsqdmbQI-65pA?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Data Council

40.9K subscribers

[The Model is the Product](https://www.youtube.com/watch?v=4dUFIRj-BWo)

Data Council

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

**“The model is NOT the product”:**

The Model is Not the Product - YouTube

[Photo image of Data Council](https://www.youtube.com/channel/UCAezwIIm1SfsqdmbQI-65pA?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Data Council

40.9K subscribers

[The Model is Not the Product](https://www.youtube.com/watch?v=EEw2PpL-_NM)

Data Council

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/will-these-evaluation-methods-still-be-relevant-in-5-10-years-given-how-fast-ai-is-changing.html)

# Error Analysis & Data Collection

## Q: Why is "error analysis" so important in LLM evals, and how is it performed? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed)

Error analysis is **the most important activity in evals**. Error analysis helps you decide what evals to write in the first place. It allows you to identify failure modes unique to your application and data. The process involves:

### 1\. Creating a Dataset [Anchor](https://hamel.dev/blog/posts/evals-faq/\#creating-a-dataset)

Gathering representative traces of user interactions with the LLM. If you do not have any data, you can [generate synthetic data](https://hamel.dev/blog/posts/evals-faq/#q-what-is-the-best-approach-for-generating-synthetic-data) to get started.

### 2\. Open Coding [Anchor](https://hamel.dev/blog/posts/evals-faq/\#open-coding)

Human annotator(s) (ideally a [benevolent dictator](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs)) review and write open-ended notes about traces, noting any issues. This process is akin to “journaling” and is adapted from qualitative research methodologies. When beginning, it is recommended to focus on noting the [first failure](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-debug-multi-turn-conversation-traces) observed in a trace, as upstream errors can cause downstream issues, though you can also tag all independent failures if feasible. A [domain expert](https://hamel.dev/blog/posts/llm-judge/#step-1-find-the-principal-domain-expert) should be performing this step.

### 3\. Axial Coding [Anchor](https://hamel.dev/blog/posts/evals-faq/\#axial-coding)

Categorize the open-ended notes into a “failure taxonomy.”. In other words, group similar failures into distinct categories. This is the most important step. At the end, count the number of failures in each category. You can use a LLM to help with this step.

### 4\. Iterative Refinement [Anchor](https://hamel.dev/blog/posts/evals-faq/\#iterative-refinement)

Keep iterating on more traces until you reach [theoretical saturation](https://delvetool.com/blog/theoreticalsaturation), meaning new traces do not seem to reveal new failure modes or information to you. As a rule of thumb, you should aim to review at least 100 traces.

You should frequently revisit this process. There are advanced ways to [sample data more efficiently](https://hamel.dev/blog/posts/evals-faq/how-can-i-efficiently-sample-production-traces-for-review.html), like clustering, sorting by user feedback, and sorting by high probability failure patterns. Over time, you’ll develop a “nose” for where to look for failures in your data.

Do not skip error analysis. It ensures that the evaluation metrics you develop are supported by real application behaviors instead of counter-productive generic metrics (which most platforms nudge you to use). For examples of how error analysis can be helpful, see [this video](https://www.youtube.com/watch?v=e2i6JbU2R-s), or this [blog post](https://hamel.dev/blog/posts/field-guide/).

Here is a visualization of the error analysis process by one of our students, [Pawel Huryn](https://www.linkedin.com/in/pawel-huryn/) \- including how it fits into the overall evaluation process:

![](https://hamel.dev/blog/posts/evals-faq/pawel-error-analysis.png)

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)

## Q: How do I surface problematic traces for review beyond user feedback? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-surface-problematic-traces-for-review-beyond-user-feedback)

While user feedback is a good way to narrow in on problematic traces, other methods are also useful. Here are three complementary approaches:

### Start with random sampling [Anchor](https://hamel.dev/blog/posts/evals-faq/\#start-with-random-sampling)

The simplest approach is reviewing a random sample of traces. If you find few issues, escalate to stress testing: create queries that deliberately test your prompt constraints to see if the AI follows your rules.

### Use evals for initial screening [Anchor](https://hamel.dev/blog/posts/evals-faq/\#use-evals-for-initial-screening)

Use existing evals to find problematic traces and potential issues. Once you’ve identified these, you can proceed with the typical evaluation process starting with [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed).

### Leverage efficient sampling strategies [Anchor](https://hamel.dev/blog/posts/evals-faq/\#leverage-efficient-sampling-strategies)

For more sophisticated trace discovery, [use outlier detection, metric-based sorting, and stratified sampling](https://hamel.dev/blog/posts/evals-faq/#q-how-can-i-efficiently-sample-production-traces-for-review) to find interesting traces. [Generic metrics can serve as exploration signals](https://hamel.dev/blog/posts/evals-faq/#q-should-i-use-ready-to-use-evaluation-metrics) to identify traces worth reviewing, even if they don’t directly measure quality.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-surface-problematic-traces-for-review-beyond-user-feedback.html)

## Q: How often should I re-run error analysis on my production system? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-often-should-i-re-run-error-analysis-on-my-production-system)

Re-run [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) when making significant changes: new features, prompt updates, model switches, or major bug fixes. A useful heuristic is to set a goal for reviewing _at least_ 100+ fresh traces each review cycle. Typical review cycles we’ve seen range from 2-4 weeks. See [this FAQ](https://hamel.dev/blog/posts/evals-faq/#q-how-can-i-efficiently-sample-production-traces-for-review) on how to sample traces effectively.

Between major analyses, review 10-20 traces weekly, focusing on outliers: unusually long conversations, sessions with multiple retries, or traces flagged by automated monitoring. Adjust frequency based on system stability and usage growth. New systems need weekly analysis until failure patterns stabilize. Mature systems might need only monthly analysis unless usage patterns change. Always analyze after incidents, user complaint spikes, or metric drift. Scaling usage introduces new edge cases.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-often-should-i-re-run-error-analysis-on-my-production-system.html)

## Q: What is the best approach for generating synthetic data? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-is-the-best-approach-for-generating-synthetic-data)

A common mistake is prompting an LLM to `"give me test queries"` without structure, resulting in generic, repetitive outputs. A structured approach using dimensions produces far better synthetic data for testing LLM applications.

**Start by defining dimensions**: categories that describe different aspects of user queries. Each dimension captures one type of variation in user behavior. For example:

- For a recipe app, dimensions might include Dietary Restriction ( _vegan_, _gluten-free_, _none_), Cuisine Type ( _Italian_, _Asian_, _comfort food_), and Query Complexity ( _simple request_, _multi-step_, _edge case_).
- For a customer support bot, dimensions could be Issue Type ( _billing_, _technical_, _general_), Customer Mood ( _frustrated_, _neutral_, _happy_), and Prior Context ( _new issue_, _follow-up_, _resolved_).

**Start with failure hypotheses**. If you lack intuition about failure modes, use your application extensively or recruit friends to use it. Then choose dimensions targeting those likely failures.

**Create tuples manually first**: Write 20 tuples by hand—specific combinations selecting one value from each dimension. Example: ( _Vegan_, _Italian_, _Multi-step_). This manual work helps you understand your problem space.

**Scale with two-step generation**:

1. **Generate structured tuples**: Have the LLM create more combinations like ( _Gluten-free_, _Asian_, _Simple_)
2. **Convert tuples to queries**: In a separate prompt, transform each tuple into natural language

This separation avoids repetitive phrasing. The ( _Vegan_, _Italian_, _Multi-step_) tuple becomes: `"I need a dairy-free lasagna recipe that I can prep the day before."`

### Generation approaches [Anchor](https://hamel.dev/blog/posts/evals-faq/\#generation-approaches)

You can generate tuples two ways:

**Cross product then filter**: Generate all dimension combinations, then filter with an LLM. Guarantees coverage including edge cases. Use when most combinations are valid.

**Direct LLM generation**: Ask the LLM to generate tuples directly. More realistic but tends toward generic outputs and misses rare scenarios. Use when many dimension combinations are invalid.

**Fix obvious problems first**: Don’t generate synthetic data for issues you can fix immediately. If your prompt doesn’t mention dietary restrictions, fix the prompt rather than generating specialized test queries.

After iterating on your tuples and prompts, **run these synthetic queries through your actual system to capture full traces**. Sample 100 traces for error analysis. This number provides enough traces to manually review and identify failure patterns without being overwhelming.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-is-the-best-approach-for-generating-synthetic-data.html)

## Q: Are there scenarios where synthetic data may not be reliable? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-are-there-scenarios-where-synthetic-data-may-not-be-reliable)

Yes: synthetic data can mislead or mask issues. For guidance on generating synthetic data when appropriate, see [What is the best approach for generating synthetic data?](https://hamel.dev/blog/posts/evals-faq/#q-what-is-the-best-approach-for-generating-synthetic-data)

Common scenarios where synthetic data fails:

1. **Complex domain-specific content**: LLMs often miss the structure, nuance, or quirks of specialized documents (e.g., legal filings, medical records, technical forms). Without real examples, critical edge cases are missed.

2. **Low-resource languages or dialects**: For low-resource languages or dialects, LLM-generated samples are often unrealistic. Evaluations based on them won’t reflect actual performance.

3. **When validation is impossible**: If you can’t verify synthetic sample realism (due to domain complexity or lack of ground truth), real data is important for accurate evaluation.

4. **High-stakes domains**: In high-stakes domains (medicine, law, emergency response), synthetic data often lacks subtlety and edge cases. Errors here have serious consequences, and manual validation is difficult.

5. **Underrepresented user groups**: For underrepresented user groups, LLMs may misrepresent context, values, or challenges. Synthetic data can reinforce biases in the training data of the LLM.


[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/are-there-scenarios-where-synthetic-data-may-not-be-reliable.html)

## Q: How do I approach evaluation when my system handles diverse user queries? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-approach-evaluation-when-my-system-handles-diverse-user-queries)

> Complex applications often support vastly different query patterns—from “What’s the return policy?” to “Compare pricing trends across regions for products matching these criteria.” Each query type exercises different system capabilities, leading to confusion on how to design eval criteria.

**_[Error Analysis](https://youtu.be/e2i6JbU2R-s?si=8p5XVxbBiioz69Xc) is all you need._** Your evaluation strategy should emerge from observed failure patterns (e.g. error analysis), not predetermined query classifications. Rather than creating a massive evaluation matrix covering every query type you can imagine, let your system’s actual behavior guide where you invest evaluation effort.

During error analysis, you’ll likely discover that certain query categories share failure patterns. For instance, all queries requiring temporal reasoning might struggle regardless of whether they’re simple lookups or complex aggregations. Similarly, queries that need to combine information from multiple sources might fail in consistent ways. These patterns discovered through error analysis should drive your evaluation priorities. It could be that query category is a fine way to group failures, but you don’t know that until you’ve analyzed your data.

To see an example of basic error analysis in action, [see this video](https://youtu.be/e2i6JbU2R-s?si=8p5XVxbBiioz69Xc).

Error Analysis: The Highest ROI Technique In AI Engineering - YouTube

[Photo image of Hamel Husain](https://www.youtube.com/channel/UC__dUuqF5w4OnbW221JxmKg?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Hamel Husain

11.1K subscribers

[Error Analysis: The Highest ROI Technique In AI Engineering](https://www.youtube.com/watch?v=e2i6JbU2R-s)

Hamel Husain

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-approach-evaluation-when-my-system-handles-diverse-user-queries.html)

## Q: How can I efficiently sample production traces for review? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-can-i-efficiently-sample-production-traces-for-review)

It can be cumbersome to review traces randomly, especially when most traces don’t have an error. These sampling strategies help you find traces more likely to reveal problems:

- **Outlier detection:** Sort by any metric (response length, latency, tool calls) and review extremes.
- **User feedback signals:** Prioritize traces with negative feedback, support tickets, or escalations.
- **Metric-based sorting:** Generic metrics can serve as exploration signals to find interesting traces. Review both high and low scores and treat them as exploration clues. Based on what you learn, you can build custom evaluators for the failure modes you find.
- **Stratified sampling:** Group traces by key dimensions (user type, feature, query category) and sample from each group.
- **Embedding clustering:** Generate embeddings of queries and cluster them to reveal natural groupings. Sample proportionally from each cluster, but oversample small clusters for edge cases. There’s no right answer for clustering—it’s an exploration technique to surface patterns you might miss manually.

As you get more sophisticated with how you sample, you can incorporate these tactics into the design of your [annotation tools](https://hamel.dev/blog/posts/evals-faq/#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-can-i-efficiently-sample-production-traces-for-review.html)

# Evaluation Design & Methodology

## Q: Why do you recommend binary (pass/fail) evaluations instead of 1-5 ratings (Likert scales)? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales)

> Engineers often believe that Likert scales (1-5 ratings) provide more information than binary evaluations, allowing them to track gradual improvements. However, this added complexity often creates more problems than it solves in practice.

Binary evaluations force clearer thinking and more consistent labeling. Likert scales introduce significant challenges: the difference between adjacent points (like 3 vs 4) is subjective and inconsistent across annotators, detecting statistical differences requires larger sample sizes, and annotators often default to middle values to avoid making hard decisions.

Having binary options forces people to make a decision rather than hiding uncertainty in middle values. Binary decisions are also faster to make during error analysis - you don’t waste time debating whether something is a 3 or 4.

For tracking gradual improvements, consider measuring specific sub-components with their own binary checks rather than using a scale. For example, instead of rating factual accuracy 1-5, you could track “4 out of 5 expected facts included” as separate binary checks. This preserves the ability to measure progress while maintaining clear, objective criteria.

Start with binary labels to understand what ‘bad’ looks like. Numeric labels are advanced and usually not necessary.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales.html)

## Q: Should I practice eval-driven development? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-practice-eval-driven-development)

**Generally no.** Eval-driven development (writing evaluators before implementing features) sounds appealing but creates more problems than it solves. Unlike traditional software where failure modes are predictable, LLMs have infinite surface area for potential failures. You can’t anticipate what will break.

A better approach is to start with [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed). Write evaluators for errors you discover, not errors you imagine. This avoids getting blocked on what to evaluate and prevents wasted effort on metrics that have no impact on actual system quality.

**Exception:** Eval-driven development may work for specific constraints where you know exactly what success looks like. If adding “never mention competitors,” writing that evaluator early may be acceptable.

Most importantly, always do a [cost-benefit analysis](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-automated-evaluators-for-every-failure-mode-i-find) before implementing an eval. Ask whether the failure mode justifies the investment. Error analysis reveals which failures actually matter for your users.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-practice-eval-driven-development.html)

## Q: Should I build automated evaluators for every failure mode I find? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-build-automated-evaluators-for-every-failure-mode-i-find)

Focus automated evaluators on failures that persist after fixing your prompts. Many teams discover their LLM doesn’t meet preferences they never actually specified - like wanting short responses, specific formatting, or step-by-step reasoning. Fix these obvious gaps first before building complex evaluation infrastructure.

Consider the cost hierarchy of different evaluator types. Simple assertions and reference-based checks (comparing against known correct answers) are cheap to build and maintain. LLM-as-Judge evaluators require 100+ labeled examples, ongoing weekly maintenance, and coordination between developers, PMs, and domain experts. This cost difference should shape your evaluation strategy.

Only build expensive evaluators for problems you’ll iterate on repeatedly. Since LLM-as-Judge comes with significant overhead, save it for persistent generalization failures - not issues you can fix trivially. Start with cheap code-based checks where possible: regex patterns, structural validation, or execution tests. Reserve complex evaluation for subjective qualities that can’t be captured by simple rules.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-build-automated-evaluators-for-every-failure-mode-i-find.html)

## Q: Should I use "ready-to-use" evaluation metrics? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-use-ready-to-use-evaluation-metrics)

**No. Generic evaluations waste time and create false confidence.** (Unless you’re using them for exploration).

One instructor noted:

> “All you get from using these prefab evals is you don’t know what they actually do and in the best case they waste your time and in the worst case they create an illusion of confidence that is unjustified.” [1](https://hamel.dev/blog/posts/evals-faq/#fn1)

Generic evaluation metrics are everywhere. Eval libraries contain scores like helpfulness, coherence, quality, etc. promising easy evaluation. These metrics measure abstract qualities that may not matter for your use case. Good scores on them don’t mean your system works.

Instead, conduct [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) to understand failures. Define [binary failure modes](https://hamel.dev/blog/posts/evals-faq/#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales) based on real problems. Create [custom evaluators](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-automated-evaluators-for-every-failure-mode-i-find) for those failures and validate them against human judgment. Essentially, the entire evals process.

Experienced practitioners may still use these metrics, just not how you’d expect. As Picasso said: “Learn the rules like a pro, so you can break them like an artist.” Once you understand why generic metrics fail as evaluations, you can repurpose them as exploration tools to [find interesting traces](https://hamel.dev/blog/posts/evals-faq/#q-how-can-i-efficiently-sample-production-traces-for-review) (explained in the next FAQ).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-use-ready-to-use-evaluation-metrics.html)

## Q: Are similarity metrics (BERTScore, ROUGE, etc.) useful for evaluating LLM outputs? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-are-similarity-metrics-bertscore-rouge-etc.-useful-for-evaluating-llm-outputs)

Generic metrics like BERTScore, ROUGE, cosine similarity, etc. are not useful for evaluating LLM outputs in most AI applications. Instead, we recommend using [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) to identify metrics specific to your application’s behavior. We recommend designing [binary pass/fail](https://hamel.dev/blog/posts/evals-faq/#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales).) evals (using LLM-as-judge) or code-based assertions.

As an example, consider a real estate CRM assistant. Suggesting showings that aren’t available (can be tested with an assertion) or confusing client personas (can be tested with a LLM-as-judge) is problematic . Generic metrics like similarity or verbosity won’t catch this. A relevant quote from the course:

> “The abuse of generic metrics is endemic. Many eval vendors promote off the shelf metrics, which ensnare engineers into superfluous tasks.”

Similarity metrics aren’t always useless. They have utility in domains like search and recommendation (and therefore can be useful for [optimizing and debugging retrieval](https://hamel.dev/blog/posts/evals-faq/#q-how-should-i-approach-evaluating-my-rag-system) for RAG). For example, cosine similarity between embeddings can measure semantic closeness in retrieval systems, and average pairwise similarity can assess output diversity (where lower similarity indicates higher diversity).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/are-similarity-metrics-bertscore-rouge-etc-useful-for-evaluating-llm-outputs.html)

## Q: Can I use the same model for both the main task and evaluation? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-can-i-use-the-same-model-for-both-the-main-task-and-evaluation)

For LLM-as-Judge selection, using the same model is usually fine because the judge is doing a different task than your main LLM pipeline. The judges we recommend building do [scoped binary classification tasks](https://hamel.dev/blog/posts/evals-faq/#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales). Focus on achieving high True Positive Rate (TPR) and True Negative Rate (TNR) with your judge on a held out labeled test set rather than avoiding the same model family. You can use these metrics on the test set to understand how well your judge is doing.

When selecting judge models, start with the most capable models available to establish strong alignment with human judgments. You can optimize for cost later once you’ve established reliable evaluation criteria. We do not recommend using the same model for open ended preferences or response quality (but we don’t recommend building judges this way in the first place!).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/can-i-use-the-same-model-for-both-the-main-task-and-evaluation.html)

* * *

**👉 _If you want to learn more about AI Evals, check out our [AI Evals course](https://bit.ly/evals-ai)_**. Here is a [35% discount code](https://bit.ly/evals-ai) for readers. 👈

* * *

# Human Annotation & Process

## Q: How many people should annotate my LLM outputs? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-many-people-should-annotate-my-llm-outputs)

For most small to medium-sized companies, appointing a single domain expert as a “benevolent dictator” is the most effective approach. This person—whether it’s a psychologist for a mental health chatbot, a lawyer for legal document analysis, or a customer service director for support automation—becomes the definitive voice on quality standards.

A single expert eliminates annotation conflicts and prevents the paralysis that comes from “too many cooks in the kitchen”. The benevolent dictator can incorporate input and feedback from others, but they drive the process. If you feel like you need five subject matter experts to judge a single interaction, it’s a sign your product scope might be too broad.

However, larger organizations or those operating across multiple domains (like a multinational company with different cultural contexts) may need multiple annotators. When you do use multiple people, you’ll need to measure their agreement using metrics like Cohen’s Kappa, which accounts for agreement beyond chance. However, use your judgment. Even in larger companies, a single expert is often enough.

Start with a benevolent dictator whenever feasible. Only add complexity when your domain demands it.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-many-people-should-annotate-my-llm-outputs.html)

## Q: Should product managers and engineers collaborate on error analysis? How? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-product-managers-and-engineers-collaborate-on-error-analysis-how)

At the outset, collaborate to establish shared context. Engineers catch technical issues like retrieval issues and tool errors. PMs identify product failures like unmet user expectations, confusing responses, or missing features users expect.

As time goes on you should lean towards a [benevolent dictator](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs) for error analysis: a domain expert or PM who understands user needs. Empower domain experts to evaluate actual outcomes rather than technical implementation. Ask “Has an appointment been made?” not “Did the tool call succeed?” The best way to empower the domain expert is to give them [custom annotation tools](https://hamel.dev/blog/posts/evals-faq/#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs) that display system outcomes alongside traces. Show the confirmation, generated email, or database update that validates goal completion. Keep all context on one screen so non-technical reviewers focus on results.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-product-managers-and-engineers-collaborate-on-error-analysis-how.html)

## Q: Should I outsource annotation & labeling to a third party? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-outsource-annotation-labeling-to-a-third-party)

Outsourcing [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) is usually a big mistake (with some [exceptions](https://hamel.dev/blog/posts/evals-faq/#exceptions-for-external-help)). The core of evaluation is building the product intuition that only comes from systematically analyzing your system’s failures. You should be extremely skeptical of this process being delegated.

### **The Dangers of Outsourcing** [Anchor](https://hamel.dev/blog/posts/evals-faq/\#the-dangers-of-outsourcing)

When you outsource annotation, you often break the feedback loop between observing a failure and understanding how to improve the product. Problems with outsourcing include:

- Superficial Labeling: Even well-defined metrics require nuanced judgment that external teams lack. A critical misstep in error analysis is excluding domain experts from the labeling process. Outsourcing this task to those without domain expertise, like general developers or IT staff, often leads to superficial or incorrect labeling.

- Loss of Unspoken Knowledge: A principal domain expert possesses tacit knowledge and user understanding that cannot be fully captured in a rubric. Involving these experts helps uncover their preferences and expectations, which they might not be able to fully articulate upfront.

- Annotation Conflicts and Misalignment: Without a shared context, external annotators can create more disagreement than they resolve. Achieving alignment is a challenge even for internal teams, which means you will spend even more time on this process.

### **The Recommended Approach: Build Internal Capability** [Anchor](https://hamel.dev/blog/posts/evals-faq/\#the-recommended-approach-build-internal-capability)

Instead of outsourcing, focus on building an efficient internal evaluation process.

1\. Appoint a “Benevolent Dictator”. For most teams, the most effective strategy is to appoint a [single, internal domain expert](https://hamel.dev/blog/posts/evals-faq/#q-how-many-people-should-annotate-my-llm-outputs) as the final decision-maker on quality. This individual sets the standard, ensures consistency, and develops a sense of ownership.

2\. Use a collaborative workflow for multiple annotators. If multiple annotators are necessary, follow a structured process to ensure alignment: \* Draft an initial rubric with clear Pass/Fail definitions and examples. \* Have each annotator label a shared set of traces independently to surface differences in interpretation. \* Measure Inter-Annotator Agreement (IAA) using a chance-corrected metric like Cohen’s Kappa. \* Facilitate alignment sessions to discuss disagreements and refine the rubric. \* Iterate on this process until agreement is consistently high.

### **How to Handle Capacity Constraints** [Anchor](https://hamel.dev/blog/posts/evals-faq/\#how-to-handle-capacity-constraints)

Building internal capacity does not mean you have to label every trace. Use these strategies to manage the workload:

- Smart Sampling: Review a small, representative sample of traces thoroughly. It is more effective to analyze 100 diverse traces to find patterns than to superficially label thousands.

- The “Think-Aloud” Protocol: To make the most of limited expert time, use this technique from usability testing. Ask an expert to verbalize their thought process while reviewing a handful of traces. This method can uncover deep insights in a single one-hour session.

- Build Lightweight Custom Tools: Build [custom annotation tools](https://hamel.dev/blog/posts/evals-faq/#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs) to streamline the review process, increasing throughput.

### **Exceptions for External Help** [Anchor](https://hamel.dev/blog/posts/evals-faq/\#exceptions-for-external-help)

While outsourcing the core error analysis process is not recommended, there are some scenarios where external help is appropriate:

- Purely Mechanical Tasks: For highly objective, unambiguous tasks like identifying a phone number or validating an email address, external annotators can be used after a rigorous internal process has defined the rubric.

- Tasks Without Product Context: Well-defined tasks that don’t require understanding your product’s specific requirements can be outsourced. Translation is a good example: it requires linguistic expertise but not deep product knowledge.

- Engaging Subject Matter Experts: Hiring external SMEs to act as your internal domain experts is not outsourcing; it is bringing the necessary expertise into your evaluation process. For example, [AnkiHub](https://www.ankihub.net/) hired 4th-year medical students to evaluate their RAG systems for medical content rather than outsourcing to generic annotators.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-outsource-annotation-and-labeling-to-a-third-party.html)

## Q: What parts of evals can be automated with LLMs? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-parts-of-evals-can-be-automated-with-llms)

LLMs can speed up parts of your eval workflow, but they can’t replace human judgment where your expertise is essential. For example, if you let an LLM handle all of [error analysis](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html) (i.e., reviewing and annotating traces), you might overlook failure cases that matter for your product. Suppose users keep mentioning “lag” in feedback, but the LLM lumps these under generic “performance issues” instead of creating a “latency” category. You’d miss a recurring complaint about slow response times and fail to prioritize a fix.

That said, LLMs are valuable tools for accelerating certain parts of the evaluation workflow _when used with oversight_.

### Here are some areas where LLMs can help: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#here-are-some-areas-where-llms-can-help)

- **First-pass axial coding:** After you’ve open coded 30–50 traces yourself, use an LLM to organize your raw failure notes into proposed groupings. This helps you quickly spot patterns, but always review and refine the clusters yourself. _Note: If you aren’t familiar with axial and open coding, see [this faq](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)._
- **Mapping annotations to failure modes:** Once you’ve defined failure categories, you can ask an LLM to suggest which categories apply to each new trace (e.g., “Given this annotation: \[open\_annotation\] and these failure modes: \[list\_of\_failure\_modes\], which apply?”).

- **Suggesting prompt improvements:** When you notice recurring problems, have the LLM propose concrete changes to your prompts. Review these suggestions before adopting any changes.

- **Analyzing annotation data:** Use LLMs or AI-powered notebooks to find patterns in your labels, such as “reports of lag increase 3x during peak usage hours” or “slow response times are mostly reported from users on mobile devices.”

### However, you shouldn’t outsource these activities to an LLM: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#however-you-shouldnt-outsource-these-activities-to-an-llm)

- **Initial open coding:** Always read through the raw traces yourself at the start. This is how you discover new types of failures, understand user pain points, and build intuition about your data. Never skip this or delegate it.

- **Validating failure taxonomies:** LLM-generated groupings need your review. For example, an LLM might group both “app crashes after login” and “login takes too long” under a single “login issues” category, even though one is a stability problem and the other is a performance problem. Without your intervention, you’d miss that these issues require different fixes.

- **Ground truth labeling:** For any data used for testing/validating LLM-as-Judge evaluators, hand-validate each label. LLMs can make mistakes that lead to unreliable benchmarks.

- **Root cause analysis:** LLMs may point out obvious issues, but only human review will catch patterns like errors that occur in specific workflows or edge cases—such as bugs that happen only when users paste data from Excel.

In conclusion, start by examining data manually to understand what’s actually going wrong. Use LLMs to scale what you’ve learned, not to avoid looking at data.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-parts-of-evals-can-be-automated-with-llms.html)

## Q: Should I stop writing prompts manually in favor of automated tools? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-stop-writing-prompts-manually-in-favor-of-automated-tools)

Automating prompt engineering can be tempting, but you should be skeptical of tools that promise to optimize prompts for you, especially in early stages of development. When you write a prompt, you are forced to clarify your assumptions and externalize your requirements. Good writing is good thinking [2](https://hamel.dev/blog/posts/evals-faq/#fn2). If you delegate this task to an automated tool too early, you risk never fully understanding your own requirements or the model’s failure modes.

This is because automated prompt optimization typically hill-climb a predefined evaluation metric. It can refine a prompt to perform better on known failures, but it cannot discover _new_ ones. Discovering new errors requires [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed). Furthermore, research shows that evaluation criteria tends to shift after reviewing a model’s outputs, a phenomenon known as “criteria drift” [3](https://hamel.dev/blog/posts/evals-faq/#fn3). This means that evaluation is an iterative, human-driven sensemaking process, not a static target that can be set once and handed off to an optimizer.

A pragmatic approach is to use LLMs to improve your prompt based on [open coding](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) (open-ended notes about traces). This way, you maintain a human in the loop who is looking at the data and externalizing their requirements. Once you have a high-quality set of evals, prompt optimization can be effective for that last mile of performance.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-stop-writing-prompts-manually-in-favor-of-automated-tools.html)

# Tools & Infrastructure

## Q: Should I build a custom annotation tool or use something off-the-shelf? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf)

**Build a custom annotation tool.** This is the single most impactful investment you can make for your AI evaluation workflow. With AI-assisted development tools like Cursor or Lovable, you can build a tailored interface in hours. I often find that teams with custom annotation tools iterate ~10x faster.

Custom tools excel because:

- They show all your context from multiple systems in one place
- They can render your data in a product specific way (images, widgets, markdown, buttons, etc.)
- They’re designed for your specific workflow (custom filters, sorting, progress bars, etc.)

Off-the-shelf tools may be justified when you need to coordinate dozens of distributed annotators with enterprise access controls. Even then, many teams find the configuration overhead and limitations aren’t worth it.

[Isaac’s Anki flashcard annotation app](https://youtu.be/fA4pe9bE0LY) shows the power of custom tools—handling 400+ results per query with keyboard navigation and domain-specific evaluation criteria that would be nearly impossible to configure in a generic tool.

Building Eval Tools with FastHTML - YouTube

[Photo image of Hamel Husain](https://www.youtube.com/channel/UC__dUuqF5w4OnbW221JxmKg?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Hamel Husain

11.1K subscribers

[Building Eval Tools with FastHTML](https://www.youtube.com/watch?v=fA4pe9bE0LY)

Hamel Husain

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf.html)

## Q: What makes a good custom interface for reviewing LLM outputs? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-makes-a-good-custom-interface-for-reviewing-llm-outputs)

Great interfaces make human review fast, clear, and motivating. We recommend [building your own annotation tool](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf) customized to your domain. The following features are possible enhancements we’ve seen work well, but you don’t need all of them. The screenshots shown are illustrative examples to clarify concepts. In practice, I rarely implement all these features in a single app. It’s ultimately a judgment call based on your specific needs and constraints.

### **1\. Render Traces Intelligently, Not Generically**: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#render-traces-intelligently-not-generically)

Present the trace in a way that’s intuitive for the domain. If you’re evaluating generated emails, render them to look like emails. If the output is code, use syntax highlighting. Allow the reviewer to see the full trace (user input, tool calls, and LLM reasoning), but keep less important details in collapsed sections that can be expanded. Here is an example of a custom annotation tool for reviewing real estate assistant emails:

![](https://hamel.dev/blog/posts/evals-faq/images/emailinterface1.png)

A custom interface for reviewing emails for a real estate assistant.

### **2\. Show Progress and Support Keyboard Navigation**: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#show-progress-and-support-keyboard-navigation)

Keep reviewers in a state of flow by minimizing friction and motivating completion. Include progress indicators (e.g., “Trace 45 of 100”) to keep the review session bounded and encourage completion. Enable hotkeys for navigating between traces (e.g., N for next), applying labels, and saving notes quickly. Below is an illustration of these features:

![](https://hamel.dev/blog/posts/evals-faq/images/hotkey.png)

An annotation interface with a progress bar and hotkey guide

### **3\. Trace navigation through clustering, filtering, and search**: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#trace-navigation-through-clustering-filtering-and-search)

Allow reviewers to filter traces by metadata or search by keywords. Semantic search helps find conceptually similar problems. Clustering similar traces (like grouping by user persona) lets reviewers spot recurring issues and explore hypotheses. Below is an illustration of these features:

![](https://hamel.dev/blog/posts/evals-faq/images/group1.png)

Cluster view showing groups of emails, such as property-focused or client-focused examples. Reviewers can drill into a group to see individual traces.

### **4\. Prioritize labeling traces you think might be problematic**: [Anchor](https://hamel.dev/blog/posts/evals-faq/\#prioritize-labeling-traces-you-think-might-be-problematic)

Surface traces flagged by guardrails, CI failures, or automated evaluators for review. Provide buttons to take actions like adding to datasets, filing bugs, or re-running pipeline tests. Display relevant context (pipeline version, eval scores, reviewer info) directly in the interface to minimize context switching. Below is an illustration of these ideas:

![](https://hamel.dev/blog/posts/evals-faq/images/ci.png)

A trace view that allows you to quickly see auto-evaluator verdict, add traces to dataset or open issues. Also shows metadata like pipeline version, reviewer info, and more.

### General Principle: Keep it minimal [Anchor](https://hamel.dev/blog/posts/evals-faq/\#general-principle-keep-it-minimal)

Keep your annotation interface minimal. Only incorporate these ideas if they provide a benefit that outweighs the additional complexity and maintenance overhead.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-makes-a-good-custom-interface-for-reviewing-llm-outputs.html)

## Q: What gaps in eval tooling should I be prepared to fill myself? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-what-gaps-in-eval-tooling-should-i-be-prepared-to-fill-myself)

Most eval tools handle the basics well: logging complete traces, tracking metrics, prompt playgrounds, and annotation queues. These are table stakes. Here are four areas where you’ll likely need to supplement existing tools.

Watch for vendors addressing these gaps: it’s a strong signal they understand practitioner needs.

### 1\. Error Analysis and Pattern Discovery [Anchor](https://hamel.dev/blog/posts/evals-faq/\#error-analysis-and-pattern-discovery)

After reviewing traces where your AI fails, can your tooling automatically cluster similar issues? For instance, if multiple traces show the assistant using casual language for luxury clients, you need something that recognizes this broader “persona-tone mismatch” pattern. We recommend building capabilities that use AI to suggest groupings, rewrite your observations into clearer failure taxonomies, help find similar cases through semantic search, etc.

### 2\. AI-Powered Assistance Throughout the Workflow [Anchor](https://hamel.dev/blog/posts/evals-faq/\#ai-powered-assistance-throughout-the-workflow)

The most effective workflows use AI to accelerate every stage of evaluation. During error analysis, you want an LLM helping categorize your open-ended observations into coherent failure modes. For example, you might annotate several traces with notes like “wrong tone for investor,” “too casual for luxury buyer,” etc. Your tooling should recognize these as the same underlying pattern and suggest a unified “persona-tone mismatch” category.

You’ll also want AI assistance in proposing fixes. After identifying 20 cases where your assistant omits pet policies from property summaries, can your workflow analyze these failures and suggest specific prompt modifications? Can it draft refinements to your SQL generation instructions when it notices patterns of missing WHERE clauses?

Additionally, good workflows help you conduct data analysis of your annotations and traces. I like using notebooks with AI in-the-loop like [Julius](https://julius.ai/), [Hex](https://hex.tech/) or [SolveIt](https://solveit.fast.ai/). These help me discover insights like “location ambiguity errors spike 3x when users mention neighborhood names” or “tone mismatches occur 80% more often in email generation than other modalities.”

### 3\. Custom Evaluators Over Generic Metrics [Anchor](https://hamel.dev/blog/posts/evals-faq/\#custom-evaluators-over-generic-metrics)

Be prepared to build most of your evaluators from scratch. Generic metrics like “hallucination score” or “helpfulness rating” rarely capture what actually matters for your application—like proposing unavailable showing times or omitting budget constraints from emails. In our experience, successful teams spend most of their effort on application-specific metrics.

### 4\. APIs That Support Custom Annotation Apps [Anchor](https://hamel.dev/blog/posts/evals-faq/\#apis-that-support-custom-annotation-apps)

Custom annotation interfaces [work best for most teams](https://hamel.dev/blog/posts/evals-faq/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf). This requires observability platforms with thoughtful APIs. I often have to build my own libraries and abstractions just to make bulk data export manageable. You shouldn’t have to paginate through thousands of requests or handle timeout-prone endpoints just to get your data. Look for platforms that provide true bulk export capabilities and, crucially, APIs that let you write annotations back efficiently.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/what-gaps-in-eval-tooling-should-i-be-prepared-to-fill-myself.html)

## Q: Seriously Hamel. Stop the bullshit. What’s your favorite eval vendor? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-seriously-hamel.-stop-the-bullshit.-whats-your-favorite-eval-vendor)

Eval tools are in an intensely competitive space. It would be futile to compare their features. If I tried to do such an analysis, it would be invalidated in a week! Vendors I encounter the most organically in my work are: [Langsmith](https://www.langchain.com/langsmith), [Arize](https://arize.com/) and [Braintrust](https://www.braintrust.dev/).

When I help clients with vendor selection, the decision weighs heavily towards who can offer the best support, as opposed to purely features. This changes depending on size of client, use case, etc. Yes - it’s mainly the human factor that matters, and dare I say, vibes.

I have no favorite vendor. At the core, their features are very similar - and I often build [custom tools](https://hamel.dev/blog/posts/evals/#q-should-i-build-a-custom-annotation-tool-or-use-something-off-the-shelf) on top of them to fit my needs.

My suggestion is to explore the vendors and see which one you like the most.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/seriously-hamel-stop-the-bullshit-whats-your-favorite-eval-vendor.html)

# Production & Deployment

## Q: How are evaluations used differently in CI/CD vs. monitoring production? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-are-evaluations-used-differently-in-cicd-vs.-monitoring-production)

The most important difference between CI vs. production evaluation is the data used for testing.

Test datasets for CI are small (in many cases 100+ examples) and purpose-built. Examples cover core features, regression tests for past bugs, and known edge cases. Since CI tests are run frequently, the cost of each test has to be carefully considered (that’s why you carefully curate the dataset). Favor assertions or other deterministic checks over LLM-as-judge evaluators.

For evaluating production traffic, you can sample live traces and run evaluators against them asynchronously. Since you usually lack reference outputs on production data, you might rely more on on more expensive reference-free evaluators like LLM-as-judge. Additionally, track confidence intervals for production metrics. If the lower bound crosses your threshold, investigate further.

These two systems are complementary: when production monitoring reveals new failure patterns through error analysis and evals, add representative examples to your CI dataset. This mitigates regressions on new issues.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-are-evaluations-used-differently-in-cicd-vs-monitoring-production.html)

## Q: What’s the difference between guardrails & evaluators? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-whats-the-difference-between-guardrails-evaluators)

Guardrails are **inline safety checks** that sit directly in the request/response path. They validate inputs or outputs _before_ anything reaches a user, so they typically are:

- **Fast and deterministic** – typically a few milliseconds of latency budget.
- **Simple and explainable** – regexes, keyword block-lists, schema or type validators, lightweight classifiers.
- **Targeted at clear-cut, high-impact failures** – PII leaks, profanity, disallowed instructions, SQL injection, malformed JSON, invalid code syntax, etc.

If a guardrail triggers, the system can redact, refuse, or regenerate the response. Because these checks are user-visible when they fire, false positives are treated as production bugs; teams version guardrail rules, log every trigger, and monitor rates to keep them conservative.

On the other hand, evaluators typically run **after** a response is produced. Evaluators measure qualities that simple rules cannot, such as factual correctness, completeness, etc. Their verdicts feed dashboards, regression tests, and model-improvement loops, but they do not block the original answer.

Evaluators are usually run asynchronously or in batch to afford heavier computation such as a [LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/). Inline use of an LLM-as-Judge is possible _only_ when the latency budget and reliability targets allow it. Slow LLM judges might be feasible in a cascade that runs on the minority of borderline cases.

Apply guardrails for immediate protection against objective failures requiring intervention. Use evaluators for monitoring and improving subjective or nuanced criteria. Together, they create layered protection.

Word of caution: Do not use llm guardrails off the shelf blindly. Always [look at the prompt](https://hamel.dev/blog/posts/prompt/).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/whats-the-difference-between-guardrails-evaluators.html)

## Q: Can my evaluators also be used to automatically _fix_ or _correct_ outputs in production? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-can-my-evaluators-also-be-used-to-automatically-fix-or-correct-outputs-in-production)

Yes, but only a specific subset of them. This is the distinction between an **evaluator** and a **guardrail** that we [previously discussed](https://hamel.dev/blog/posts/evals-faq/#q-whats-the-difference-between-guardrails-evaluators). As a reminder:

- **Evaluators** typically run _asynchronously_ after a response has been generated. They measure quality but don’t interfere with the user’s immediate experience.

- **Guardrails** run _synchronously_ in the critical path of the request, before the output is shown to the user. Their job is to prevent high-impact failures in real-time.

There are two important decision criteria for deciding whether to use an evaluator as a guardrail:

1. **Latency & Cost**: Can the evaluator run fast enough and cheaply enough in the critical request path without degrading user experience?

2. **Error Rate Trade-offs**: What’s the cost-benefit balance between false positives (blocking good outputs and frustrating users) versus false negatives (letting bad outputs reach users and causing harm)? In high-stakes domains like medical advice, false negatives may be more costly than false positives. In creative applications, false positives that block legitimate creativity may be more harmful than occasional quality issues.


Most guardrails are designed to be **fast** (to avoid harming user experience) and have a **very low false positive rate** (to avoid blocking valid responses). For this reason, you would almost never use a slow or non-deterministic LLM-as-Judge as a synchronous guardrail. However, these tradeoffs might be different for your use case.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/can-my-evaluators-also-be-used-to-automatically-fix-or-correct-outputs-in-production.html)

## Q: How much time should I spend on model selection? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-much-time-should-i-spend-on-model-selection)

Many developers fixate on model selection as the primary way to improve their LLM applications. Start with error analysis to understand your failure modes before considering model switching. As Hamel noted in office hours, “I suggest not thinking of switching model as the main axes of how to improve your system off the bat without evidence. Does error analysis suggest that your model is the problem?”

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-much-time-should-i-spend-on-model-selection.html)

# Domain-Specific Applications

## Q: Is RAG dead? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-is-rag-dead)

Question: Should I avoid using RAG for my AI application after reading that [“RAG is dead”](https://pashpashpash.substack.com/p/why-i-no-longer-recommend-rag-for) for coding agents?

> Many developers are confused about when and how to use RAG after reading articles claiming “RAG is dead.” Understanding what RAG actually means versus the narrow marketing definitions will help you make better architectural decisions for your AI applications.

The viral article claiming RAG is dead specifically argues against using _naive vector database retrieval_ for autonomous coding agents, not RAG as a whole. This is a crucial distinction that many developers miss due to misleading marketing.

RAG simply means Retrieval-Augmented Generation - using retrieval to provide relevant context that improves your model’s output. The core principle remains essential: your LLM needs the right context to generate accurate answers. The question isn’t whether to use retrieval, but how to retrieve effectively.

For coding applications, naive vector similarity search often fails because code relationships are complex and contextual. Instead of abandoning retrieval entirely, modern coding assistants like Claude Code [still uses retrieval](https://x.com/pashmerepat/status/1926717705660375463?s=46) —they just employ agentic search instead of relying solely on vector databases, similar to how human developers work.

You have multiple retrieval strategies available, ranging from simple keyword matching to embedding similarity to LLM-powered relevance filtering. The optimal approach depends on your specific use case, data characteristics, and performance requirements. Many production systems combine multiple strategies or use multi-hop retrieval guided by LLM agents.

Unfortunately, “RAG” has become a buzzword with no shared definition. Some people use it to mean any retrieval system, others restrict it to vector databases. Focus on the ultimate goal: getting your LLM the context it needs to succeed. Whether that’s through vector search, agentic exploration, or hybrid approaches is a product and engineering decision.

Rather than following categorical advice to avoid or embrace RAG, experiment with different retrieval approaches and measure what works best for your application. For more info on RAG evaluation and optimization, see [this series of posts](https://hamel.dev/notes/llm/rag/not_dead.html).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/is-rag-dead.html)

## Q: How should I approach evaluating my RAG system? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-should-i-approach-evaluating-my-rag-system)

RAG systems have two distinct components that require different evaluation approaches: retrieval and generation.

The retrieval component is a search problem. Evaluate it using traditional information retrieval (IR) metrics. Common examples include Recall@k (of all relevant documents, how many did you retrieve in the top k?), Precision@k (of the k documents retrieved, how many were relevant?), or MRR (how high up was the first relevant document?). The specific metrics you choose depend on your use case. These metrics are pure search metrics that measure whether you’re finding the right documents (more on this below).

To evaluate retrieval, create a dataset of queries paired with their relevant documents. Generate this synthetically by taking documents from your corpus, extracting key facts, then generating questions those facts would answer. This reverse process gives you query-document pairs for measuring retrieval performance without manual annotation.

For the generation component—how well the LLM uses retrieved context, whether it hallucinates, whether it answers the question—use the same evaluation procedures covered throughout this course: error analysis to identify failure modes, collecting human labels, building LLM-as-judge evaluators, and validating those judges against human annotations.

Jason Liu’s [“There Are Only 6 RAG Evals”](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/) provides a framework that maps well to this separation. His Tier 1 covers traditional IR metrics for retrieval. Tiers 2 and 3 evaluate relationships between Question, Context, and Answer—like whether the context is relevant (C\|Q), whether the answer is faithful to context (A\|C), and whether the answer addresses the question (A\|Q).

In addition to Jason’s six evals, error analysis on your specific data may reveal domain-specific failure modes that warrant their own metrics. For example, a medical RAG system might consistently fail to distinguish between drug dosages for adults versus children, or a legal RAG might confuse jurisdictional boundaries. These patterns emerge only through systematic review of actual failures. Once identified, you can create targeted evaluators for these specific issues beyond the general framework.

Finally, when implementing Jason’s Tier 2 and 3 metrics, don’t just use prompts off the shelf. The standard LLM-as-judge process requires several steps: error analysis, prompt iteration, creating labeled examples, and measuring your judge’s accuracy against human labels. Once you know your judge’s True Positive and True Negative rates, you can correct its estimates to determine the actual failure rate in your system. Skip this validation and your judges may not reflect your actual quality criteria.

In summary, debug retrieval first using IR metrics, then tackle generation quality using properly validated LLM judges.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-should-i-approach-evaluating-my-rag-system.html)

## Q: How do I choose the right chunk size for my document processing tasks? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-choose-the-right-chunk-size-for-my-document-processing-tasks)

Unlike RAG, where chunks are optimized for retrieval, document processing assumes the model will see every chunk. The goal is to split text so the model can reason effectively without being overwhelmed. Even if a document fits within the context window, it might be better to break it up. Long inputs can degrade performance due to attention bottlenecks, especially in the middle of the context. Two task types require different strategies:

### 1\. Fixed-Output Tasks → Large Chunks [Anchor](https://hamel.dev/blog/posts/evals-faq/\#fixed-output-tasks-large-chunks)

These are tasks where the output length doesn’t grow with input: extracting a number, answering a specific question, classifying a section. For example:

- “What’s the penalty clause in this contract?”
- “What was the CEO’s salary in 2023?”

Use the largest chunk (with caveats) that likely contains the answer. This reduces the number of queries and avoids context fragmentation. However, avoid adding irrelevant text. Models are sensitive to distraction, especially with large inputs. The middle parts of a long input might be under-attended. Furthermore, if cost and latency are a bottleneck, you should consider preprocessing or filtering the document (via keyword search or a lightweight retriever) to isolate relevant sections before feeding a huge chunk.

### 2\. Expansive-Output Tasks → Smaller Chunks [Anchor](https://hamel.dev/blog/posts/evals-faq/\#expansive-output-tasks-smaller-chunks)

These include summarization, exhaustive extraction, or any task where output grows with input. For example:

- “Summarize each section”
- “List all customer complaints”

In these cases, smaller chunks help preserve reasoning quality and output completeness. The standard approach is to process each chunk independently, then aggregate results (e.g., map-reduce). When sizing your chunks, try to respect content boundaries like paragraphs, sections, or chapters. Chunking also helps mitigate output limits. By breaking the task into pieces, each piece’s output can stay within limits.

### General Guidance [Anchor](https://hamel.dev/blog/posts/evals-faq/\#general-guidance)

It’s important to recognize **why chunk size affects results**. A larger chunk means the model has to reason over more information in one go – essentially, a heavier cognitive load. LLMs have limited capacity to **retain and correlate details across a long text**. If too much is packed in, the model might prioritize certain parts (commonly the beginning or end) and overlook or “forget” details in the middle. This can lead to overly coarse summaries or missed facts. In contrast, a smaller chunk bounds the problem: the model can pay full attention to that section. You are trading off **global context for local focus**.

No rule of thumb can perfectly determine the best chunk size for your use case – **you should validate with experiments**. The optimal chunk size can vary by domain and model. I treat chunk size as a hyperparameter to tune.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-choose-the-right-chunk-size-for-my-document-processing-tasks.html)

## Q: How do I debug multi-turn conversation traces? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-debug-multi-turn-conversation-traces)

Start simple. Check if the whole conversation met the user’s goal with a pass/fail judgment. Look at the entire trace and focus on the first upstream failure. Read the user-visible parts first to understand if something went wrong. Only then dig into the technical details like tool calls and intermediate steps.

### Multi-agent trace logging [Anchor](https://hamel.dev/blog/posts/evals-faq/\#multi-agent-trace-logging)

For multi-agent flows, assign a session or trace ID to each user request and log every message with its source (which agent or tool), trace ID, and position in the sequence. This lets you reconstruct the full path from initial query to final result across all agents.

### Annotation strategy [Anchor](https://hamel.dev/blog/posts/evals-faq/\#annotation-strategy)

Annotate only the first failure in the trace initially—don’t worry about downstream failures since these often cascade from the first issue. Fixing upstream failures often resolves dependent downstream failures automatically. As you gain experience, you can annotate independent failure modes within the same trace to speed up overall error analysis.

### Simplify when possible [Anchor](https://hamel.dev/blog/posts/evals-faq/\#simplify-when-possible)

When you find a failure, reproduce it with the simplest possible test case. Here’s an example: suppose a shopping bot gives the wrong return policy on turn 4 of a conversation. Before diving into the full multi-turn complexity, simplify it to a single turn: “What is the return window for product X1000?” If it still fails, you’ve proven the error isn’t about conversation context - it’s likely a basic retrieval or knowledge issue you can debug more easily.

### Test case generation [Anchor](https://hamel.dev/blog/posts/evals-faq/\#test-case-generation)

You have two main approaches. First, simulate users with another LLM to create realistic multi-turn conversations. Second, use “N-1 testing” where you provide the first N-1 turns of a real conversation and test what happens next. The N-1 approach often works better since it uses actual conversation prefixes rather than fully synthetic interactions, but is less flexible.

The key is balancing thoroughness with efficiency. Not every multi-turn failure requires multi-turn analysis.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-debug-multi-turn-conversation-traces.html)

## Q: How do I evaluate sessions with human handoffs? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-evaluate-sessions-with-human-handoffs)

Capture the complete user journey in your traces, including human handoffs. The trace continues until the user’s need is resolved or the session ends, not when AI hands off to a human. Log the handoff decision, why it occurred, context transferred, wait time, human actions, final resolution, and whether the human had sufficient context. Many failures occur at handoff boundaries where AI hands off too early, too late, or without proper context.

Evaluate handoffs as potential failure modes during [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed). Ask: Was the handoff necessary? Did the AI provide adequate context? Track both handoff quality and handoff rate. Sometimes the best improvement reduces handoffs entirely rather than improving handoff execution.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-sessions-with-human-handoffs.html)

## Q: How do I evaluate complex multi-step workflows? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-evaluate-complex-multi-step-workflows)

Log the entire workflow from initial trigger to final business outcome. Include LLM calls, tool usage, human approvals, and database writes in your traces. You will need this visibility to properly diagnose failures.

Use both outcome and process metrics. Outcome metrics verify the final result meets requirements: Was the business case complete? Accurate? Properly formatted? Process metrics evaluate efficiency: step count, time taken, resource usage. Process failures are often easier to debug since they’re more deterministic, so tackle them first.

Segment your [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed) by workflow stages. Early stage failures (understanding user input) differ from middle stage failures (data processing) and late stage failures (formatting output). Early stage improvements have more impact since errors cascade in LLM chains.

Use [transition failure matrices](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-evaluate-agentic-workflows) to analyze where workflows break. Create a matrix showing the last successful state versus where the first failure occurred. This reveals failure hotspots and guides where to invest debugging effort.

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-complex-multi-step-workflows.html)

## Q: How do I evaluate agentic workflows? [Anchor](https://hamel.dev/blog/posts/evals-faq/\#q-how-do-i-evaluate-agentic-workflows)

We recommend evaluating agentic workflows in two phases:

**1\. End-to-end task success.** Treat the agent as a black box and ask “did we meet the user’s goal?”. Define a precise success rule per task (exact answer, correct side-effect, etc.) and measure with human or [aligned LLM judges](https://hamel.dev/blog/posts/llm-judge/). Take note of the first upstream failure when conducting [error analysis](https://hamel.dev/blog/posts/evals-faq/#q-why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed).

Once error analysis reveals which workflows fail most often, move to step-level diagnostics to understand why they’re failing.

**2\. Step-level diagnostics.** Assuming that you have sufficiently [instrumented your system](https://hamel.dev/blog/posts/evals/#logging-traces) with details of tool calls and responses, you can score individual components such as: - _Tool choice_: was the selected tool appropriate? - _Parameter extraction_: were inputs complete and well-formed? - _Error handling_: did the agent recover from empty results or API failures? - _Context retention_: did it preserve earlier constraints? - _Efficiency_: how many steps, seconds, and tokens were spent? - _Goal checkpoints_: for long workflows verify key milestones.

Example: “Find Berkeley homes under $1M and schedule viewings” breaks into: parameters extracted correctly, relevant listings retrieved, availability checked, and calendar invites sent. Each checkpoint can pass or fail independently, making debugging tractable.

**Use transition failure matrices to understand error patterns.** Create a matrix where rows represent the last successful state and columns represent where the first failure occurred. This is a great way to understand where the most failures occur.

![](https://hamel.dev/blog/posts/evals-faq/images/shreya_matrix.png)

Transition failure matrix showing hotspots in text-to-SQL agent workflow

Transition matrices transform overwhelming agent complexity into actionable insights. Instead of drowning in individual trace reviews, you can immediately see that GenSQL → ExecSQL transitions cause 12 failures while DecideTool → PlanCal causes only 2. This data-driven approach guides where to invest debugging effort. Here is another [example](https://www.figma.com/deck/nwRlh5renu4s4olaCsf9lG/Failure-is-a-Funnel?node-id=2009-927&t=GJlTtxQ8bLJaQ92A-1) from Bryan Bischof, that is also a text-to-SQL agent:

![](https://hamel.dev/blog/posts/evals-faq/images/bischof_matrix.png)

Bischof, Bryan “Failure is A Funnel - Data Council, 2025”

In this example, Bryan shows variation in transition matrices across experiments. How you organize your transition matrix depends on the specifics of your application. For example, Bryan’s text-to-SQL agent has an inherent sequential workflow which he exploits for further analytical insight. You can watch his [full talk](https://youtu.be/R_HnI9oTv3c?si=hRRhDiydHU5k6ikc) for more details.

Stop Managing AI Projects Like Traditional Software - YouTube

[Photo image of Hamel Husain](https://www.youtube.com/channel/UC__dUuqF5w4OnbW221JxmKg?embeds_referring_euri=https%3A%2F%2Fhamel.dev%2F)

Hamel Husain

11.1K subscribers

[Stop Managing AI Projects Like Traditional Software](https://www.youtube.com/watch?v=R_HnI9oTv3c)

Hamel Husain

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

**Creating Test Cases for Agent Failures**

Creating test cases for agent failures follows the same principles as our previous FAQ on [debugging multi-turn conversation traces](https://hamel.dev/blog/posts/evals-faq/#q-how-do-i-debug-multi-turn-conversation-traces) (i.e. try to reproduce the error in the simplest way possible, only use multi-turn tests when the failure actually requires conversation context, etc.).

[↗ Focus view](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html)

* * *

**👉 _If you want to learn more about AI Evals, check out our [AI Evals course](https://bit.ly/evals-ai)_**. Here is a [35% discount code](https://bit.ly/evals-ai) for readers. 👈

* * *

## Footnotes [Anchor](https://hamel.dev/blog/posts/evals-faq/\#footnotes-1)

1. [Eleanor Berger](https://www.linkedin.com/in/intellectronica/), our wonderful TA. [↩︎](https://hamel.dev/blog/posts/evals-faq/#fnref1)

2. Paul Graham, [“Writes and Write-Nots”](https://paulgraham.com/writes.html) [↩︎](https://hamel.dev/blog/posts/evals-faq/#fnref2)

3. Shreya Shankar, et al., [“Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences”](https://arxiv.org/abs/2404.12272) [↩︎](https://hamel.dev/blog/posts/evals-faq/#fnref3)