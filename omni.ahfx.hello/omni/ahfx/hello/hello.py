import omni.ext

import carb.events
import omni.usd


# Functions and vars are available to other extension as usual in python: `omni.ahfx.hello.some_public_function(x)`
def some_public_function(x: int):
    print(f"[omni.ahfx.hello] some_public_function was called with {x}")
    return x ** x

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class HelloExtension(omni.ext.IExt):

    def __init__(self):
        self._keyboard_sub_id = None

    def on_input(self, event):
        """The keyboard callback"""

        stage = omni.usd.get_context().get_stage()
        layer = stage.GetRootLayer()
        print(stage, layer)

        print(f"omni.ahfx.hello Input Event: {event.type} {event.input} {event.modifiers}")
        return True

    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.ahfx.hello] AHFX Extension startup")

        appwindow = omni.appwindow.get_default_app_window()
        keyboard = appwindow.get_keyboard()
        input = carb.input.acquire_input_interface()
        self._keyboard_sub_id = input.subscribe_to_keyboard_events(keyboard, self.on_input)

    def on_shutdown(self):
        print("[omni.ahfx.hello] AHFX Extension shutdown")

        appwindow = omni.appwindow.get_default_app_window()
        keyboard = appwindow.get_keyboard()
        input = carb.input.acquire_input_interface()
        input.unsubscribe_to_keyboard_events(keyboard, self._keyboard_sub_id)
        self._keyboard_sub_id = None