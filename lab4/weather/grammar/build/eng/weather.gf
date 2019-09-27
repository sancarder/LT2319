abstract weather = TDM, Integers ** {

cat

Sort_city;
Sort_domain;
Predicate_country_to_search;
Sort_string;
Sort_country;
Predicate_city_to_search;
Predicate_weather;
Predicate_temperature;
Unknown;

fun

top : VpAction;
top_request_1 : Predicate_city_to_search -> UsrRequest;
up : VpAction;
city_london : Sort_city;
country_uk : Sort_country;
city_to_search : Predicate;
city_to_search_sys_answer : Sort_city -> SysAnswer;
city_to_search_sortal_usr_answer : Sort_city -> UsrAnswer;
city_to_search_propositional_usr_answer : Sort_city -> Predicate_city_to_search;
city_user_answer : Sort_city -> UsrAnswer;
city_individual : Sort_city -> Individual;
weather : Predicate;
weather_resolve_ynq_2 : SysResolveGoal;
ask_weather : UsrWHQ;
weather_sys_answer_0 : SysAnswer;
weather_sys_answer_1 : SysAnswer;
weather_sys_answer_2 : SysAnswer;
weather_sys_answer_3 : SysAnswer;
weather_sys_answer_4 : SysAnswer;
weather_sys_answer_5 : SysAnswer;
weather_sys_answer_6 : SysAnswer;
weather_sys_answer_7 : SysAnswer;
weather_sys_answer_8 : SysAnswer;
weather_sys_answer_9 : SysAnswer;
weather_sortal_usr_answer : Sort_string -> UsrAnswer;
weather_propositional_usr_answer : Unknown -> Predicate_weather;
country_to_search : Predicate;
country_to_search_sys_answer : Sort_country -> SysAnswer;
country_to_search_sortal_usr_answer : Sort_country -> UsrAnswer;
country_to_search_propositional_usr_answer : Sort_country -> Predicate_country_to_search;
country_user_answer : Sort_country -> UsrAnswer;
country_individual : Sort_country -> Individual;
temperature : Predicate;
temperature_resolve_ynq_3 : SysResolveGoal;
ask_temperature : UsrWHQ;
temperature_user_question_4 : Predicate_city_to_search -> Predicate_country_to_search -> UsrWHQ;
temperature_sys_answer_0 : SysAnswer;
temperature_sys_answer_1 : SysAnswer;
temperature_sys_answer_2 : SysAnswer;
temperature_sys_answer_3 : SysAnswer;
temperature_sys_answer_4 : SysAnswer;
temperature_sys_answer_5 : SysAnswer;
temperature_sys_answer_6 : SysAnswer;
temperature_sys_answer_7 : SysAnswer;
temperature_sys_answer_8 : SysAnswer;
temperature_sys_answer_9 : SysAnswer;
temperature_sortal_usr_answer : Sort_string -> UsrAnswer;
temperature_propositional_usr_answer : Unknown -> Predicate_temperature;
mkUnknown : String -> Unknown;
unknown_string : Unknown -> Sort_string;
}
