import pkg_resources


def get_handlers(group):
    handlers = []
    for dist in pkg_resources.working_set:
        entries = dist.get_entry_map(group)
        for full_name, entry in entries.items():
            handlers.append(entry)
    return handlers

handlers = []
# NOTE:  Entry points are yielded from the active distributions in the order 
#        that the distributions appear in the working set. See docs.
entry_points = list(pkg_resources.iter_entry_points("mydomain.myplugin"))[::-1]
for entry_point in entry_points:
    handler = entry_point.load()
    handlers.append(handler())


print(handlers)
assert ['a', 'b', 'c', 'd', 'e'] == handlers