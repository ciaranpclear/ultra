from enigma_app.formatting.formatting import EnigmaFormatter as ef
from enigma_core.scrambler.exceptions.exceptions import RingCharacterError
from enigma_core.validators.scrambler_validators.scrambler_validators import *
from enigma_app.clear_terminal.clear_terminal import clear_terminal


class ScramblerInterface:

    def __init__(self, machine_type, scrambler_obj):
        """
        
        """
        self.machine_type = machine_type
        self._scrambler_obj = scrambler_obj
        self._collection = scrambler_obj.collection

    def __str__(self):
        """
        
        """
        return ef.center(self._scrambler_obj.__str__())

    def menu(self):
        """
        
        """
        while True:

            menu_str = (
                f"{ef.line('SCRAMBLER')}\n\n{self}\n\n"
                f"Enter a number to select an option\n"
                f"1. Display collection\n"
                f"2. Select reflector\n"
                f"3. Select rotors\n"
                f"4. Set rotor settings\n"
                f"5. Set ring settings\n"
                f"6. Clear scrambler\n"
                f"7. Return to previous menu\n"
                f"{ef.line()}\n"
            )

            inpt = input(menu_str)
            if inpt == "1":
                clear_terminal()
                print(self._collection)
            elif inpt == "2":
                clear_terminal()
                self._select_reflector()
            elif inpt == "3":
                clear_terminal()
                self._select_rotor_types()
            elif inpt == "4":
                clear_terminal()
                self._select_rotor_settings()
            elif inpt == "5":
                clear_terminal()
                self._select_ring_settings()
            elif inpt == "6":
                clear_terminal()
                self._clear_scrambler()
            elif inpt == "7":
                clear_terminal()
                break
            else: print("Invalid input! Try agin")

    def character_set_flag(self, flag):
        """
        
        """
        self._scrambler_obj.character_set_flag = flag

    def _select_reflector(self):
        """
        
        """
        machine = self._scrambler_obj.machine

        reflectors = self._collection.device_list(machine, ["REF"])

        menu_str = "Enter a number to select a reflector.\n"

        for index, reflector in enumerate(reflectors, start=1):
            menu_str += f"{index}. {reflector}\n"
        menu_str += f"{len(reflectors)+1}. Quit\n"

        while True:
            clear_terminal()
            try:
                inpt = int(input(menu_str))
            except ValueError:
                print("Invalid input!. Try again.")
            else:
                if 1 <= inpt <= len(reflectors):
                    reflector = reflectors[inpt-1]
                    self._scrambler_obj.set_device("REF", reflector)
                    if reflector == "UKW-D":
                        reflector_obj = self._scrambler_obj.get_device("REF")
                        self._wire_reflector(reflector_obj)
                    clear_terminal()
                elif inpt == len(reflectors)+1:
                    clear_terminal()
                    break
                else:
                    print("Invalid input!. Try again.")

    def _wire_reflector(self, reflector_obj):
        """
        
        """
        clear_terminal()

        charset_flag = self._scrambler_obj.character_set_flag

        current_wire_list = reflector_obj.wire_characters

        format = "Z,A,B,C,D" if charset_flag == "L" else "02,03,04,05"

        if charset_flag == "L":
            header = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif charset_flag == "N":
            header = "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"

        while True:
            print(f"Current reflector wiring\n{','.join(current_wire_list)}\n")
            inpt = input(f"Enter the reflector wiring list in the format {format}... or q to return to previous menu.\n{header}\n")

            if inpt.upper() == "Q":
                break

            try:
                wire_list = ScramblerValidators.valid_reflector_wiring(inpt, charset_flag)
            except ReflectorWireStringError as e:
                clear_terminal()
                print(e)
            else:
                reflector_obj.set_wiring(wire_list)
                break

    def _select_rotor_types(self):
        """
        
        """
        # prompt user for rotor type for each rotor position.
        # check rotor type is valid and compatible with that position.
        # check all rotors are unique.
        # set rotor types.
        machine = self._scrambler_obj.machine

        dynamic_rotors = self._collection.device_list(machine, ["R_ROT"])
        static_rotors = self._collection.device_list(machine, ["F_ROT"])
        rotors_signature = self._collection.device_signature(machine, ["R_ROT","F_ROT"])

        selected_rotors = {position:None for position in rotors_signature.keys()}

        positions = list(rotors_signature.keys())
        positions.reverse()

        while True:
            for position in positions:
                clear_terminal()
                menu_str = (
                    f"Enter a number to select a rotor for rotor position {position}.\n"
                )

                if rotors_signature[position] == "R_ROT":
                    rotors_list = dynamic_rotors
                elif rotors_signature[position] == "F_ROT":
                    rotors_list = static_rotors
                
                for index, rotor in enumerate(rotors_list, start=1):
                    menu_str += f"{index}. {rotor}\n"
                menu_str += f"{len(rotors_list)+1}. Quit\n"

                try:
                    inpt = int(input(menu_str))
                except ValueError:
                    print("Invalid input!. Try again.")
                else:
                    if 1 <= inpt <= len(rotors_list):
                        rotor = rotors_list[inpt-1]
                        if rotor in selected_rotors.values():
                            for _position, _rotor in selected_rotors.items():
                                if rotor == _rotor:
                                    selected_rotors[_position] = None
                        selected_rotors[position] = rotor
                    elif inpt == len(rotors_list)+1:
                        return
                    else:
                        print("Invalid input!. Try again.")

            if None not in selected_rotors.values():
                clear_terminal()
                break

        self._scrambler_obj.rotor_types = selected_rotors

    def _select_rotor_settings(self):
        """
        
        """
        # prompt user for rotor setting for each rotor position.
        # check setting is a valid rotor setting.
        # set rotor settings.
        rotor_settings = self._get_settings("rotor")

        if rotor_settings:
            self._scrambler_obj.rotor_settings = rotor_settings
        else:
            return

    def _select_ring_settings(self):
        """
        
        """
        # prompt user for ring position for each rotor position.
        # check setting is a valid ring setting.
        # set ring settings.
        ring_settings = self._get_settings("ring")

        if ring_settings:
            self._scrambler_obj.ring_settings = ring_settings
        else:
            return

    def _get_settings(self, settings_str):
        """
        
        """
        rotor_types = self._scrambler_obj.rotor_types

        if None in rotor_types.values():
            unset = [pos for pos in rotor_types.keys() if rotor_types[pos] == None]
            unset_str = ",".join(unset)
            print(f"No rotor(s) set at rotor positions {unset_str}. "
                  f"All rotors must be set before {settings_str} settings can be selected.")
            return None

        settings = {position:None for position in rotor_types.keys()}

        char_set_flag = self._scrambler_obj.character_set_flag

        range_str = "A-Z" if char_set_flag == 'L' else "01-26"

        positions = list(rotor_types.keys())
        positions.reverse()

        for position in positions:
            while True:
                clear_terminal()
                menu_str = (
                    f"Enter a {settings_str} setting for rotor position "
                    f"{position} in the range {range_str}.\n"
                )

                rotor_setting = input(menu_str)

                try:
                    rotor_setting = ScramblerValidators.valid_ring_character(rotor_setting, char_set_flag)
                except RingCharacterError:
                    print("Invalid input!. Try again.")
                else:
                    settings[position] = rotor_setting
                    clear_terminal()
                    break

        return settings

    def _clear_scrambler(self):
        """
        
        """
        while True:
            clear_terminal()
            inpt = input("Are you sure you want to clear the scrambler Y/N.\n")

            if inpt.upper() == 'Y':
                self._scrambler_obj.clear_scrambler()
            break
