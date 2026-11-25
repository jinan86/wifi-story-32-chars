"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes one Wi-Fi network name to /output/entry.txt (or a path given
as the first argument). The name is a single fixed string, chosen
because it lands a joke on the first read and implies a whole story:
a millionaire -- a character with money -- is still stealing the
neighbour's Wi-Fi -- the situation and the thing that happened.
Stdlib only, deterministic, no network, no randomness.
"""

# The entry: 30 characters, UTF-8, not whitespace-only.
# "Millionaire." names the character and his situation (rich).
# "Still Steals WiFi" is the twist and the event: he moochs the
# neighbour's network anyway. A stranger reading a phone's network
# list gets the whole miniature story in one line.
ENTRY = "Millionaire. Still Steals WiFi"


def main(argv):
    """Write ENTRY to the output path (default /output/entry.txt)."""
    path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    text = ENTRY
    if not (1 <= len(text) <= 32):
        raise SystemExit("entry must be 1-32 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be whitespace only")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    import sys

    main(sys.argv)
