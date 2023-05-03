from data_structures.hashtable import Hashtable

def left_join(hash1, hash2):
    hashtable = Hashtable()
    hash1_keys = hash1.keys()
    hash2_keys = hash2.keys()

    for key in hash1_keys:
        value = [hash1[key],]
        if key in hash2_keys:
            value.append(hash2[key])
        else:
            value.append(None)

        hashtable.set(key, value)

    return hashtable

if __name__ == "__main__":
    synonyms = {
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }


    hash = left_join(synonyms, antonyms)
    print(hash)
