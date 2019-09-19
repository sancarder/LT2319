abstract call_john = TDM, Integers ** {

cat

Predicate_phone_number;
Sort_phone;
Sort_domain;
Sort_contact;
Predicate_phone_type;
Sort_number;
Predicate_selected_contact;

fun

top : VpAction;
call : VpAction;
call_request_1 : Predicate_selected_contact -> Predicate_phone_type -> UsrRequest;
call_request_2 : Predicate_selected_contact -> UsrRequest;
up : VpAction;
placeholder_phone0 : Sort_phone;
placeholder_phone1 : Sort_phone;
placeholder_phone2 : Sort_phone;
placeholder_phone3 : Sort_phone;
placeholder_phone4 : Sort_phone;
placeholder_phone5 : Sort_phone;
placeholder_phone6 : Sort_phone;
placeholder_phone7 : Sort_phone;
placeholder_phone8 : Sort_phone;
placeholder_phone9 : Sort_phone;
placeholder_contact0 : Sort_contact;
placeholder_contact1 : Sort_contact;
placeholder_contact2 : Sort_contact;
placeholder_contact3 : Sort_contact;
placeholder_contact4 : Sort_contact;
placeholder_contact5 : Sort_contact;
placeholder_contact6 : Sort_contact;
placeholder_contact7 : Sort_contact;
placeholder_contact8 : Sort_contact;
placeholder_contact9 : Sort_contact;
placeholder_number0 : Sort_number;
placeholder_number1 : Sort_number;
placeholder_number2 : Sort_number;
placeholder_number3 : Sort_number;
placeholder_number4 : Sort_number;
placeholder_number5 : Sort_number;
placeholder_number6 : Sort_number;
placeholder_number7 : Sort_number;
placeholder_number8 : Sort_number;
placeholder_number9 : Sort_number;
mobile : Sort_phone;
home : Sort_phone;
john : Sort_contact;
work : Sort_phone;
mary : Sort_contact;
phone_number : Predicate;
phone_number_ask_whq_with_background_3 : SysAnswer -> System;
phone_number_resolve_ynq_4 : SysAnswer -> SysResolveGoal;
ask_phone_number : UsrWHQ;
phone_number_sys_answer : Sort_number -> SysAnswer;
phone_number_sortal_usr_answer : Sort_number -> UsrAnswer;
phone_number_propositional_usr_answer : Sort_number -> Predicate_phone_number;
number_user_answer : Sort_number -> UsrAnswer;
number_individual : Sort_number -> Individual;
phone_type : Predicate;
phone_type_sys_answer : Sort_phone -> SysAnswer;
phone_type_sortal_usr_answer : Sort_phone -> UsrAnswer;
phone_type_propositional_usr_answer : Sort_phone -> Predicate_phone_type;
phone_user_answer : Sort_phone -> UsrAnswer;
phone_individual : Sort_phone -> Individual;
selected_contact : Predicate;
selected_contact_sys_answer : Sort_contact -> SysAnswer;
selected_contact_sortal_usr_answer : Sort_contact -> UsrAnswer;
selected_contact_propositional_usr_answer : Sort_contact -> Predicate_selected_contact;
contact_user_answer : Sort_contact -> UsrAnswer;
contact_individual : Sort_contact -> Individual;
report_ended_Call_5 : SysAnswer -> SysAnswer -> SysReportEnded;
report_failed_Call_undefined_failure_6 : SysAnswer -> SysAnswer -> SysReportFailed;
ContactValidity_7 : SysAnswer -> SysICM;
PhoneNumberValidity_8 : SysAnswer -> SysICM;
}
