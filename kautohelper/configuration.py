
class Configure():

    def __init__(self):

        self.LIST_DEVICES = "adb devices"
        self.TAP_DEVICES = "adb -s {0} shell input tap {1} {2}"
        self.SHELL = "adb -s {0} shell {1}"
        self.SWIPE_DEVICES = "adb -s {0} shell input swipe {1} {2} {3} {4} {5}"
        self.KEY_DEVICES = "adb -s {0} shell input keyevent {1}"
        self.INPUT_TEXT_DEVICES = "adb -s {0} shell input text \"{1}\""
        self.CAPTURE_SCREEN_TO_DEVICES = "adb -s {0} shell screencap"
        self.PULL_FILE_FROM_DEVICES = "adb -s {0} pull \"{1}\" {2}"
        self.PUSH_FILE_FROM_DEVICES = "adb -s {0} push \"{1}\" {2}"
        self.REMOVE_SCREEN_FROM_DEVICES = "adb -s {0} shell rm -f \"{1}\""
        self.GET_SCREEN_RESOLUTION = "adb -s {0} shell dumpsys display | Find \"mCurrentDisplayRect\""
        self.ADB_FOLDER_PATH = ""
        self.INSTALL_APP = "adb -s {0} install {1}"
        self.UNINSTALL_APP = "adb -s {0} uninstall {1}"
        self.CLEAR_PACKAGE = "adb -s {0} shell pm clear {1}"
        self.GRANT = "adb -s {0} shell pm grant {1} {2}"
        self.OPEN_PACKAGE = "adb -s {0} shell monkey -p {1} -c android.intent.category.LAUNCHER 1"