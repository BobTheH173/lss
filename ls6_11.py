import warnings

warnings.simplefilter("ignore", SyntaxWarning)

warnings.warn("Warning, no code here", SyntaxWarning)

try:
    warnings.warn("Warning, no module found", ImportWarning)
except:
    print("except")
