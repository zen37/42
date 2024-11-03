https://www.youtube.com/watch?v=pxuXaaT1u3k

https://github.com/ArjanCodes/2023-logging

`logging.basicConfig(level=logging.INFO)` sets the default logging level for the root logger to `INFO`, which allows all loggers that do not explicitly set a level to inherit this configuration. However, when you create individual loggers, they inherit the logging level from their parent (which is the root logger), but they do not automatically get the same level you may want them to have if you don't explicitly set it.

### Why Individual Logger Levels Matter
1. **Default Level of Loggers**: When you create a new logger using `logging.getLogger()`, its level is set to `WARNING` by default unless you change it. So if you only use `logging.basicConfig(level=logging.INFO)`, any logger created without an explicit level will only log messages at the `WARNING` level and higher.

2. **Granularity of Control**: By setting the level for each logger explicitly, you gain finer control over which messages are logged. For instance, you might want to have one logger log everything from `DEBUG` level upwards, while another only logs `ERROR` level messages.

3. **Preventing Propagation**: Loggers can propagate messages to their parent loggers (including the root logger). If you don't want messages logged by your individual loggers to also be handled by the root logger, setting the propagation to `False` prevents duplicate log entries in your output.

### Summary
While `logging.basicConfig(level=logging.INFO)` sets a good default, you need to ensure each logger has the appropriate level set explicitly to capture the intended log messages. If you don’t set it for individual loggers, their default level may prevent them from logging the messages you expect.