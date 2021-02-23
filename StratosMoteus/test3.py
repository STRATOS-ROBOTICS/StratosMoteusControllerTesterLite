"""
This code was helpful,
https://stackoverflow.com/questions/32141623/pyqt5-and-asyncio-yield-from-never-finishes
"""
import os
import sys
import quamash
import asyncio
import traceback
import PyQt5
import pdb
import math
import moteus

# Required setup to get event loop working
app = PyQt5.QtWidgets.QApplication(sys.argv)
loop = quamash.QEventLoop(app)
asyncio.set_event_loop(loop)
loop.set_debug(True)  # optional


# Select QT5
# https://github.com/enthought/traitsui/issues/407
os.environ["ETS_TOOLKIT"] = "qt"
os.environ["QT_API"] = "pyqt5"
from traits.api import HasTraits, Button, Instance, Int, Bool
from traitsui.api import ModelView, View, Item, Label
from PyQt5.QtCore import pyqtRemoveInputHook

pyqtRemoveInputHook()  # enabled pdb.set_trace()    ????


class App(HasTraits):
    """ Traits application model.
    """

    running = Bool(False)

    async def test_task(self):

        c = moteus.Controller()
        await c.set_stop()  # in case there was a fault

        while True:        
           loop = asyncio.get_event_loop()
           self.running = True
           print(await c.set_position(position=math.nan, velocity=0.5, maximum_torque=0.5, stop_position=0.9, query=True))   #commande pour faire actioer position et retour indfo console 
           await asyncio.sleep(0.02, loop)
           self.running = False


class AppView(ModelView):
    """ Traits application view.
    """

    model = Instance(App)

    test_task_btn = Button("START")

    def close(self, info, is_ok):
        print("Close")
        return True

    def _test_task_btn_fired(self):
        print("Button pressed.")
        try:
            loop.create_task(self.model.test_task())
        except:
            traceback.print_exc()
            print("Problem")

    def default_traits_view(self):
        view = View(
            Label("MoteusControllerTesterLite"),
            Item("test_task_btn", show_label=False, enabled_when="not model.running"),
            resizable=True,
            title="MoteusControllerTesterLite",

        )
        return view


with loop:
    print("Launching app.")
    model = App()
    view = AppView(model=model)
    view.edit_traits()
    print("edit_traits")
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8:
        asyncio.events._set_running_loop(loop)  # Need if using >= Python 3.8
    loop.run_forever()
    print("Finished run_forever()")
print("App closed.")
