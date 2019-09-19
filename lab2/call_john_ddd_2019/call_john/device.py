from tdm.lib.device import DddDevice, DeviceAction, DeviceWHQuery, Validity, EntityRecognizer


class CallJohnDevice(DddDevice):

    JOHN = "contact_john"
    LISA = "contact_lisa"
    MARY = "contact_mary"
    ANDY = "contact_andy"

    MOBILE = "mobile"
    WORK = "work"
    HOME = "home"

    PHONE_NUMBERS = {
        JOHN: {
            MOBILE: "0701234567",
            WORK: "0736582934",
            HOME: "031122363"
        },
        LISA: {
            MOBILE: "0709876543",
            WORK: "0763559230",
            HOME: "031749205"
        },
        MARY: {
            MOBILE: "0706574839",
            WORK: "0784736475",
            HOME: "031847528"
            },
        ANDY: None
    }

    CONTACTS = {
        "John": JOHN,
        "Lisa": LISA,
        "Mary": MARY,
        "Andy": ANDY,
    }

    class Call(DeviceAction):
        def perform(self, selected_contact, phone_type):
            return True

    class phone_number(DeviceWHQuery):
        def perform(self, selected_contact, phone_type):
            number = self.device.PHONE_NUMBERS.get(selected_contact).get(phone_type)
            return [number]

    class ContactValidity(Validity):
        def is_valid(self, selected_contact):
            
            try:
                self.device.JOHN
            except Exception as e:
                return False
            return True

    class PhoneNumberValidity(Validity):
        def is_valid(self, selected_contact):
            print(selected_contact)
            
            try:
                self.device.PHONE_NUMBERS.get[selected_contact]

            except Exception as e:
                print(e.args)
                return False
            return True

    class CallJohnRecognizer(EntityRecognizer):
        def recognize(self, string, unused_language):
            result = []
            words = string.lower().split()
            for contact in self.device.CONTACTS.keys():
                if contact.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact
                    }
                    result.append(recognized_entity)
            return result
