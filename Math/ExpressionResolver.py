
import numexpr


def resolve(expr:str, **kwargs):
    for key, value in kwargs.items():
        expr = expr.replace(key, value)

    return numexpr.evaluate(expr)


if __name__ == "__main__":
    print(resolve("DPTH + (WIDA / sin(30))", DPTH="100", WIDA="200"))