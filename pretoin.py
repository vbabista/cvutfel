import re

def chyba():
    print("ERROR");exit()

def convert(vstup=str):
    if not re.fullmatch(r'[\d+\-*/\s]+', vstup):
        return chyba()

    tokens = re.findall(r'\*\*|[+\-*/]|\d+', vstup)
    if not tokens:
        return chyba()

    prec = {"+": 1, "-": 1,"*": 2, "/": 2,"**": 3}

    ops = set(prec.keys())
    N = len(tokens)

    # Prefix parser: vrací (expr, precedence)
    def parse(i):
        if i >= N:
            return None, None, i

        tok = tokens[i]

        # číslo
        if re.fullmatch(r'\d+', tok):
            return tok, 4, i + 1   # číslo má nejvyšší prioritu (už se nikdy nezávorkuje)

        # operátor
        if tok in ops:
            left_expr, left_p, ni = parse(i + 1)
            if left_expr is None:
                return None, None, i

            right_expr, right_p, nj = parse(ni)
            if right_expr is None:
                return None, None, i

            my_p = prec[tok]

            # Levá asociativita pro + - * /
            if tok != "**":
                if left_p < my_p:
                    left_expr = f"({left_expr})"
                if right_p < my_p or (right_p == my_p):
                    right_expr = f"({right_expr})"

            # Pravá asociativita pro **
            else:
                if left_p < my_p or (left_p == my_p):
                    left_expr = f"({left_expr})"
                if right_p < my_p:
                    right_expr = f"({right_expr})"

            return f"{left_expr}{tok}{right_expr}", my_p, nj

        return None, None, i

    expr, p, next_idx = parse(0)
    if expr is None or next_idx != N:
        return chyba()

    return expr

if __name__ == "__main__":
    vstup = str(input()).strip()
    out = convert(vstup)
    print(out)