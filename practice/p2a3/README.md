# Tool schemas and MCP

## Activity

Phase 2, "Tool schemas and MCP": explain tool descriptions and argument schemas, and MCP's role between host/client and server.

## Time spent

Not reported.

## Review

What it gets right:

- **Discovery:** the client lists the server's tools, with pagination for long lists.
- **A tool's fields:** a name that identifies it for calls, a display title, a description, a required input schema giving required and optional parameters, and an optional output schema.
- **The wire:** JSON-RPC 2.0 messages, an agreed protocol version, and two transports, stdio for a local server and Streamable HTTP for a remote one.

What's missing or wrong:

- **What descriptions and schemas are for.** They're written for the model, not the client. The host puts every tool's name, description and schema into the model's context. The model decides from the descriptions whether to call a tool and which one, and writes the arguments as JSON that fits the schema. The client only carries the call to the server. A description's quality decides how well the model picks tools: what the tool does, when to use it and when not, and what it returns. A schema's types, required fields, enums and parameter descriptions shape the model's arguments, and let the host validate them before anything runs.
- **The clarifying questions read as hedging.** Asking "what do you mean by role" before answering a standard question, and again after it, takes time without adding anything. Answer first, then offer to go deeper on one part.

Left for follow-up questions, which is fine at interview length (the human's choice, not to start every answer from the basics): tool schemas exist without MCP, in the model API itself; the host, which runs the model and opens one client per server, versus the client; why MCP exists, M + N integrations instead of M × N; resources, prompts and elicitation.

Verdict: **doesn't meet the activity yet.** The protocol mechanics are accurate, but the answer lists what descriptions and schemas contain without saying they're how the model chooses and calls tools. One sentence would fix it.

## Assistance used

Not reported.
