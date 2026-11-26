# One Line, Big Laugh — final version
# Writes a single hilarious line to entry.txt.
# The alarm speaks in its own voice, with numbers (214 times, three fires)
# and one twist in the final words: if it goes off, dinner is ready.
import os

ENTRY = "I am the smoke alarm. I have screamed at burnt toast 214 times and slept through three actual kitchen fires, so if I go off tonight, just assume dinner is ready."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
