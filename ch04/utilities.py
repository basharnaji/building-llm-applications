import json
import re

def to_obj(s):
    try:
        # strip markdown code fences (```json ... ``` or ``` ... ```)
        s = re.sub(r'^```(?:json)?\s*', '', s.strip(), flags=re.IGNORECASE)
        s = re.sub(r'\s*```$', '', s.strip())
        return json.loads(s)
    except Exception:
        return {}