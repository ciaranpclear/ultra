from enigma_core.settings.settings import EQUIPMENT_DICT, LETTERS, NUMBERS


class RotorSettingsDictError(Exception):

    def __init__(self, err_msg):
        """
        Takes an error message string.
        """
        super().__init__(err_msg)


class RotorSettingsDictValidator:

    POSITIONS = ["R4","RS","RM","RF"]

    def __init__(self):
        self.settings_dict = None
        self.charset_flag = None
        self.check_positions = None
        self.output_dict = None

    def validate(self, settings_dict, charset_flag, check_positions=None):
        self.settings_dict = settings_dict
        self.output_dict = {}
        self._valid_charset_flag(charset_flag)
        self._valid_settings_dict_keys()
        self._check_positions(check_positions)
        self._valid_rotor_settings()

        return self.output_dict

    def _valid_settings_dict_keys(self):
        for position, rotor_setting in self.settings_dict.items():
            if position not in self.POSITIONS:
                err_msg = f"Position {position} is not a valid position. Must be in R4,RS,RM,RF."
                raise RotorSettingsDictError(err_msg)
            else:
                self.output_dict[position] = rotor_setting

    def _valid_charset_flag(self, charset_flag):
        charset_flag = charset_flag.upper()
        if charset_flag not in ["L","N"]:
            err_msg = f"{charset_flag} is not a valid charset flag. Must be 'L' or 'N'."
            raise Exception(err_msg)
        else:
            self.charset_flag = charset_flag
        
    def _check_positions(self, check_positions):
        if check_positions:
            for position in check_positions:
                if position not in self.POSITIONS:
                    err_msg = f"Position {position} is not a valid check position. Must be in R4,RS,RM,RF."
                    raise Exception(err_msg)
            self.check_positions = check_positions
        else:
            self.check_positions = list(self.settings_dict.keys())

    def _valid_rotor_settings(self):
        err_msg = None

        for position, rotor_setting in self.settings_dict.items():
            if self.charset_flag == "L":
                rotor_setting = rotor_setting.upper()
                if position in self.check_positions:
                    if rotor_setting not in LETTERS:
                        err_msg = f"Rotor setting '{rotor_setting}' at position {position} is not a valid rotor setting. Must be letter A-Z."
                else:
                    self.output_dict[position] = rotor_setting
            if self.charset_flag == "N":
                _rotor_setting = rotor_setting.rjust(2,'0')
                if position in self.check_positions:
                    if _rotor_setting not in NUMBERS:
                        err_msg = f"Rotor setting '{rotor_setting}' at position {position} is not a valid rotor setting. Must be number 01-26."
                else:
                    self.output_dict[position] = rotor_setting
            if err_msg:
                raise RotorSettingsDictError(err_msg)
