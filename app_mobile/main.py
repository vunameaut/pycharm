from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from jnius import autoclass

DevicePolicyManager = autoclass('android.app.admin.DevicePolicyManager')
ComponentName = autoclass('android.content.ComponentName')


class TimerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Enter time to lock screen (seconds):')
        self.layout.add_widget(self.label)

        self.time_input = TextInput(multiline=False)
        self.layout.add_widget(self.time_input)

        self.start_button = Button(text='Start Timer')
        self.start_button.bind(on_press=self.start_timer)
        self.layout.add_widget(self.start_button)

        return self.layout

    def start_timer(self, instance):
        try:
            time = int(self.time_input.text)
            Clock.schedule_once(self.lock_screen, time)
        except ValueError:
            self.label.text = 'Invalid input! Please enter a number.'

    def lock_screen(self, dt):
        context = autoclass('org.kivy.android.PythonActivity').mActivity.getApplicationContext()
        dpm = context.getSystemService(context.DEVICE_POLICY_SERVICE)
        component_name = ComponentName(context, 'com.yourpackage.MyDeviceAdminReceiver')

        if dpm.isAdminActive(component_name):
            dpm.lockNow()
        else:
            self.label.text = 'Device Admin permission is not granted.'


if __name__ == '__main__':
    TimerApp().run()
