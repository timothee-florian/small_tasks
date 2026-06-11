# From ML Model to AI Agent
### Hands-on workshop — building a fraud-detection assistant from scratch
*Machine learning + AI agents · ~2 hours*

---

## Slide 1 · Title

# From ML Model to AI Agent

**Hands-on workshop** — building a fraud-detection assistant from scratch.
Machine learning + AI agents · ~2 hours.

> **Speaker notes:** Welcome. In two hours we build an ML fraud model and an AI agent, then combine them. Run the cells, watch what happens, ask questions.

---

## Slide 2 · Agenda — What we'll build today

| Part | Focus | Time |
|------|-------|------|
| **Part 1 · The Agent** | Build an AI agent with simple tools — a clock and a calculator. | ~30 min |
| **Part 2 · The ML Model** | Train a real fraud detector and learn why accuracy can mislead. | ~40 min |
| **Part 3 · Combining Them** | Plug the trained model into the agent as a tool. | ~25 min |
| **Part 4 · Recap** | What we built, what it means, and where it applies in banking. | ~10 min |

> **Speaker notes:** Four parts. Agent-first because a calculator tool is instantly understood; the fraud model then has a clear purpose. Bonus cells at the end of each part.

---

## Slide 3 · An agent is an LLM that can use tools

*Part 1 · The Agent*

**A plain chatbot** — takes your message, returns words. It can describe what to do, but it can't actually do anything.

**An AI agent** — decides which tool to call, runs it, reads the result, and keeps reasoning until the task is done.

**The agent loop:**

```
User asks
    │
    ▼
LLM thinks: need a tool?  ──►  Tool runs, returns result
    │                                    │
    │           (loops until done)       │
    ▼ ◄──────────────────────────────────┘
Final answer
```

> *The loop never changes. Tools are what make it powerful.*

> **Speaker notes:** Key mental model: the reasoning loop is fixed. You extend the agent by giving it tools, not by rewriting its logic.

---

## Slide 4 · Same agent, different tools

To the agent, every capability is the same kind of thing — a function it can choose to call.

| Tool | Example prompt |
|------|----------------|
| 🕐 **Clock** | "What time is it in Tokyo?" |
| 🧮 **Calculator** | "What's 12% of €4,200?" |
| ⚠️ **Fraud predictor** | "Is this transaction fraud?" |

We start with a clock and a calculator — then ask: what if the tool were a real fraud model?

> **Speaker notes:** Live: agent calls clock, calculator, then a placeholder fraud tool returning a hardcoded 0.87. That hollow value motivates Part 2.

---

## Slide 5 · Fraud is rare — and that breaks accuracy

*Part 2 · The ML Model*

| Stat | Meaning |
|------|---------|
| **0.17%** | of real transactions are fraudulent |
| **99.8%** | accuracy by always guessing "not fraud" |
| **0** | frauds actually caught by that "great" model |

A model can look almost perfect on accuracy and still be completely useless. We need better metrics.

```
Legitimate  ████████████████████████████████████████  99.83%
Fraud       ▏ 0.17%
```

> **Speaker notes:** Poll first: is 99.8% accuracy good? Reveal: always-"not-fraud" scores 99.8% and catches zero fraud. The accuracy trap of imbalanced data.

---

## Slide 6 · Precision vs recall: the real tradeoff

Same data, two models. Accuracy barely moves — but fraud caught jumps from almost none to most of it.

| Model | Accuracy | Fraud recall |
|-------|----------|--------------|
| Naive model | 99.8 | 1.0 |
| Balanced model | 95.0 | 82.0 |

**Precision** — Of the transactions we block, how many were truly fraud? Low precision frustrates real customers.

**Recall** — Of all real fraud, how much did we catch? Low recall means fraud slips through and customers lose money.

> **Speaker notes:** Which error is worse — blocking a real customer or missing fraud? No universal answer; it's a business decision about the cost of each mistake.

---

## Slide 7 · Why we use two datasets

**Real data** — Kaggle credit-card fraud
- ✅ Real 0.17% imbalance — the true problem
- ✅ Genuine fraud patterns to learn from
- ⚠️ Features anonymised (V1–V28) for privacy
- ⚠️ "V14 is high" means nothing to a human

**Synthetic data** — generated in the notebook
- ✅ Human-readable: amount, hour, category
- ✅ Matches exactly what the agent sends
- ✅ Lets the agent explain itself in plain English
- ✅ Safe to share — no real customer data

> **Speaker notes:** Real data for credibility and true imbalance; synthetic so the agent gets readable inputs. In production a feature pipeline bridges the two.

---

## Slide 8 · The model becomes the agent's tool

*Part 3 · Combining Them*

```
   AI Agent              Fraud model                Decision
(reasons & explains)  +  (scores the risk)   ──►   "Block it."
```

**"Block it."** — Score 0.87 — high amount, 3am, dormant account, high-risk merchant. *A plain-English decision.*

*"Transaction #312 triggered an alert. Should we block it?"* → the agent looks it up, scores it, recommends.

> **Speaker notes:** The payoff: replace the Part 1 stub with the trained model. Audience tweaks details and watches the decision change. Signals come from SHAP — the model's own reasoning.

---

## Slide 9 · One function changed. Nothing else.

This is how real AI systems are maintained — tools evolve independently of the agent that calls them.

| Component | Before (Part 1) | After (Part 3) |
|-----------|-----------------|----------------|
| **The fraud tool** | Hardcoded 0.87, always "block" | → Real model score + SHAP signals |
| **The agent loop** | unchanged | → unchanged |
| **The prompt & other tools** | unchanged | → unchanged |

> *Ship a better model tomorrow, and the agent gets better — with no change to the agent's code.*

> **Speaker notes:** Evidence for the Part 1 lesson: only the tool's internals changed. The agent is a thin reasoning layer over capabilities your teams already own.

---

## Slide 10 · Where this fits in a bank

*Part 4 · Recap*

Each is the same agent — just a different model behind the tool.

- 🔍 **AML monitoring** — Flag suspicious patterns and draft the first version of a suspicious-activity report for review.
- 📄 **Loan pre-screening** — A credit-risk model behind the tool; the agent explains each decision with an audit trail.
- 🧠 **Regulatory Q&A** — Query live risk indicators plus policy documents; answer compliance questions in plain English.

> **Speaker notes:** Open the floor: where could this fit your team? The agent stays the same; the model and data sources change.

---

## Slide 11 · Before you deploy this for real

A workshop demo and a production banking system are very different things. The hard parts aren't the code.

- 🛡️ **Human in the loop** — For consequential calls (blocking a payment, denying a loan), the agent recommends; a person decides.
- 🛡️ **Model governance** — Validation, monitoring and documentation within your model-risk framework.
- ⚖️ **Explainability & fairness** — Be able to explain automated decisions — and remember a model is only as fair as its data.
- ⚠️ **The LLM can be wrong** — Tools provide ground truth; the LLM narrates. Keep that boundary clear.

> **Speaker notes:** Important for a banking audience. This is exactly why we chose SHAP over a black-box score: explainability is a regulatory requirement.

---

## Slide 12 · The one thing to remember

# The agent loop never changes. Tools are what make it powerful.

An AI agent isn't a monolith you build once. It's a thin reasoning layer over the models, data and services your teams already have — and any one of them can become a tool.

*Now go build something.*

> **Speaker notes:** Close on the core idea: everything scales beyond fraud. Any model, data source, or service can become a tool an agent reasons with. Point them to the notebook to keep.
