import os

# Patch note announcing the fix for human sleep: on-demand sleep, with a
# known-issue twist. Single line, 89 characters, no trailing newline.
ENTRY = "Fixed: humans can now fall asleep on demand; known issue: they keep doing it in meetings."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
