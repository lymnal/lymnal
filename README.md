<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img alt="Ethan Sam — AI Engineer. LLM agents and automation systems that reach production." src="assets/banner-light.svg">
</picture>

I build LLM agents and internal tooling, and I judge a system by whether people still use it six
months later. Before that I did security research at NYU — CTFs, LLM red-teaming, digital
forensics — which is mostly why I now spend my time trying to falsify my own systems rather than
demo them.

**Currently:** mechanistic interpretability of refusal behaviour, and agent harnesses that verify
their own output.

---

### Selected work

**[NeuroScope](https://github.com/lymnal/neuroscope)** — mechanistic interpretability for GPT-2, in your browser · [`live`](https://neuroscope-interp.netlify.app)
GPT-2 runs in the tab over WebGPU; a TransformerLens backend handles logit lens, gradients, steering
and ablation. The bench compares six published refusal-ablation techniques on Llama-3.2-1B and
measures two things separately: whether the model stops refusing, and whether it still *represents*
the request as harmful, using a probe on the residual stream. The sample is small, and the results
are reported with their intervals and limits.
`TypeScript` · `WebGPU` · `TransformerLens`

**[SwarmTrace](https://github.com/lymnal/swarmtrace)** — how claims travel through a swarm of AI agents · three-person team
Built at the AI Swarm Dynamics Hackathon (October 3–4, 2026) on the AI Village dataset: 173,493 agent
messages and 2.5M logged computer actions. When one agent repeats another's claim, did it check
first? The team's pre-registered measurement study found no check in the relaying agent's logs for
21 of 49 decided relays. My part was the investigator workbench, which traces a correction from
warning to observed outcome in the original chat, tool output and screenshots.
`Python`

**[pine-auditor](https://github.com/lymnal/pine-auditor)** — static backtest-integrity audit for Pine Script
TradingView will happily report a 4,000% return on a strategy that trades on future data and pays no
commission. Deterministic rules catch that class of defect before it costs money. Run against eight
public strategies by three authors — 1,826 lines the rules were never written against — it produced
**88 findings**, each spot-checked against source; none was a false positive. Read-only: it never
sizes or recommends a trade.
`TypeScript` · `Node`

**[Couplet](https://lymnal.github.io/couplet/)** — five word games for exactly two people · [`source`](https://github.com/lymnal/couplet)
Offline-first PWA, no framework, no build step. 400 original puzzles and prompts. The hard parts are
invisible: realtime that survives a phone going to sleep, and state that reconciles after a subway
ride with no signal. I built it for two people I already knew, and every parlor still holds exactly
two.
`JavaScript` · `Supabase` · `PWA`

<sub>Also built, not public: **NYC Distress Radar** — nightly 0–100 distress scoring for ~857k NYC
properties across nine municipal datasets, with an MCP server for agents. **Anchor** — habit-tracking
iOS app on TestFlight. **Weather Edge** — Kalshi temperature-bracket pricing that grades every thesis
against what actually settled.</sub>

---

### Elsewhere

[ethansam.io](https://ethansam.io) · [LinkedIn](https://www.linkedin.com/in/ethansam) · [esam5556@gmail.com](mailto:esam5556@gmail.com)
