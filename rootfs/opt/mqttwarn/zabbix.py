def ZabbixData(topic, data, srv=None):
    client = 'unknown'
    key = None

    parts = topic.split('/')
    client = parts[1]
    key = parts[2]

    return dict(client=client, key=key)
