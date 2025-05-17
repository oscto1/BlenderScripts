import bpy
from math import radians

# Get the active object
original = bpy.context.active_object

collection_name = "Generated wheels"

# Try to get the collection if it exists, if not, create it
if collection_name in bpy.data.collections:
    my_collection = bpy.data.collections[collection_name]
else:
    my_collection = bpy.data.collections.new(collection_name)
    bpy.context.scene.collection.children.link(my_collection)

def create_duplicate(name, position, rotation, scale, collection):
    if original is None:
        raise Exception("No active object selected.")
    # Deselect everything
    bpy.ops.object.select_all(action='DESELECT')
    dup = original.copy()
    dup.data = original.data.copy()
    bpy.context.collection.objects.link(dup)

    # set transfom options
    dup.location = position
    dup.scale = scale
    dup.rotation_euler = rotation
    dup.name = name

    if collection:
        collection.objects.link(dup)
        bpy.context.collection.objects.unlink(dup)

    # Apply transforms options
    bpy.context.view_layer.objects.active = dup
    dup.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bpy.ops.object.select_all(action='DESELECT')
    return dup

def deg_to_rad(x, y, z):
    return (radians(x), radians(y), radians(z))
   

create_duplicate(name = "FL_Wheel", position = (1.7997, -2.0044, 0.74449), rotation = deg_to_rad(0, 0, 0), scale = (1.0, 1.0, 1.0), collection=my_collection)
create_duplicate(name = "FR_Wheel", position = (-1.7997, -2.0044, 0.74449), rotation = deg_to_rad(0, 180, 0), scale = (1.0, 1.0, 1.0), collection=my_collection)
create_duplicate(name = "RL_Wheel", position = (1.8865, 2.1023, 0.52301), rotation = deg_to_rad(0, 0, 0), scale = (0.683, 0.683, 0.683), collection=my_collection)
create_duplicate(name = "RR_Wheel", position = (-1.8865, 2.1023, 0.52301), rotation = deg_to_rad(0, 180, 0), scale = (0.683, 0.683, 0.683), collection=my_collection)