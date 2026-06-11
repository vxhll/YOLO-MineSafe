from pygrabber.dshow_graph import FilterGraph

graph = FilterGraph()
devices = graph.get_input_devices()

# Print without [] and ''
for device in devices:
    print(device)

