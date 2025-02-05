def helper(work):
    work_in_memory = work

    def helper(work):
        return f"I will help you with your {work_in_memory}, then with {work}"
    return helper


helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))
