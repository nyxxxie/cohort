import idb
with idb.from_file('./test.idb') as db:
    api = idb.IDAPython(db)
    for addr in api.idautils.Functions():
        print('{}: {}'.format(addr, api.idc.GetFunctionName(addr)))
