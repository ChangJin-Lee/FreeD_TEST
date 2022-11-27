from collections import defaultdict


def check_format(value) -> str:
    if not isinstance(value, dict) or isinstance(value, list):
        return "please check order format... "


def check_order(values : dict) -> bool:
    for k,v in values.items():
        if int(v) < 0:
            return False
    return True

def check_warehouse_inventory(values : list) -> bool:
    for value in values:
        for k, v in value["inventory"].items():
            if int(v) < 0:
                return False
    return True


def convert_str_to_dict(value) -> list:
    for i in range(len(value)):
        if value[i] == ' ':
            if value[i-1] == "}" and value[i+1] == "}":
                value[i] = ''
            elif value[i+1] == "{":
                value[i] = ''
            else:
                value[i] = '"'
        elif value[i] == ':':
            value[i] = '":'
        elif value[i] == ',' and value[i-1] != '}':
            value[i] = '",'
    return eval("".join(value))


def allocate_inventory(order: dict, warehouses: list) -> list:
    result = []
    for warehouse in warehouses:
        kdict = defaultdict(dict)
        for k, v in warehouse["inventory"].items():
            warehouse["inventory"][k] = int(v)
            for o, e in order.items():
                order[o] = int(e)
                mdict = defaultdict(int)
                if o == k and order[o] > 0 and warehouse["inventory"][k] != 0:
                    if order[o] >= warehouse["inventory"][k]:
                        order[o] -= warehouse["inventory"][k]
                        mdict[o] += warehouse["inventory"][k]
                    else:
                        mdict[o] += order[o]
                        order[o] = 0
                elif o == k and warehouse["inventory"][k] == 0:
                    if order[o] > warehouse["inventory"][k]:
                        return []
                if mdict:
                    kdict["name"] = warehouse["name"]
                    if kdict[warehouse["name"]]:
                        kdict[warehouse["name"]].update(dict(mdict))
                    else:
                        kdict[warehouse["name"]] = dict(mdict)
        if kdict[warehouse["name"]]:
            result.append(dict(kdict))
    result = sorted(result, key=lambda x: x['name'])
    for re in result:
        re.pop('name')
    # if order remain 
    for z in order.values():
        if z != 0:
            return []
    return result
