def find_classes(line):
    line = line[len("class "):].strip()
    class_args = line[:line.find(":")].strip()
    if "(" in class_args:
        class_name = class_args[:class_args.find("(")].strip()
        base_classes = class_args[class_args.find("(") + 1:].strip(") ").strip()
        parents_classes = [j.strip() for j in base_classes.split(",")]
    else:
        class_name = class_args
        parents_classes = ["object"]
    return class_name, parents_classes



def merge_mro_seq(sequences):
    result = []
    counter = {}
    for seq in sequences:
        for class_name in seq[1:]:
            counter[class_name] = counter.get(class_name, 0) + 1

    while True:
        sequences = [seq for seq in sequences if seq]
        if not sequences:
            return result
        candidate_found = False
        for seq in sequences:
            candidate = seq[0]
            if counter.get(candidate, 0) == 0:
                candidate_found = True
                result.append(candidate)
                for s in sequences:
                    if s and s[0] == candidate:
                        s.pop(0)
                        if len(s) >= 1:
                            next_candidate = s[0]
                            counter[next_candidate] = counter.get(next_candidate, 0) - 1
                break
        if not candidate_found:
            raise StopIteration

def test_mro(class_name, all_classes, mro_cache, visiting):
    if class_name in mro_cache:
        return mro_cache[class_name]
    if class_name in visiting:
        raise StopIteration
    visiting.add(class_name)
    if class_name not in all_classes:
        raise StopIteration
    bases = all_classes[class_name]
    mro_lists = []
    for base in bases:
        mro = test_mro(base, all_classes, mro_cache, visiting)
        mro_lists.append(mro)
    mro_lists.append(bases[:])
    merged = merge_mro_seq([list(mro) for mro in mro_lists])
    mro = [class_name] + merged
    mro_cache[class_name] = mro
    visiting.remove(class_name)
    return mro


classes = {"object": []}
while True:
    try:
        s = input()
        if not s.startswith("class "):
            continue
        tmp = find_classes(s)
        classes[tmp[0]] = tmp[1]
    except EOFError:
        break
mro_dict = {}
try:
    for i in classes:
        test_mro(i, classes, mro_dict, set())
except StopIteration:
    print("No")
else:
    print("Yes")
