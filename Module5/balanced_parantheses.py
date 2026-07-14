
def paren(s, l, r, p, n):
    # Base case: sequence is full — print the completed combination
    if(p == 2*n):
        for ss in s:
            print(ss, end='')
        print("\n")
        return

    # Close-brace branch: safe only when unmatched { exists (l > r)
    if(l > r):
        s[p] = "}"
        paren(s, l, r+1, p+1, n)

    # Open-brace branch: allowed only when more { still needed (l < n)
    if(l < n):
        s[p] = "{"
        paren(s, l+1, r, p+1, n)

# ─────────────────────────────────────────────────────────────────────

n = int(input("Enter number of parenthesis : "))
s = [""] * 2 * n
print("\n")
paren(s, 0, 0, 0, n)
