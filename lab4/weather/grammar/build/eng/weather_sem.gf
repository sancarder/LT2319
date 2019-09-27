concrete weather_sem of weather = TDM_sem, Integers_sem ** open Utils_sem in {

lincat

Sort_city = SS;
Sort_domain = SS;
Predicate_country_to_search = SS;
Sort_string = SS;
Sort_country = SS;
Predicate_city_to_search = SS;
Predicate_weather = SS;
Predicate_temperature = SS;
Unknown = SS;

lin

top = pp "top";
top_request_1 city_to_search = request (pp "top") city_to_search;
up = pp "up";
city_london = pp "city_london";
country_uk = pp "country_uk";
city_to_search = pp "city_to_search";
city_to_search_sys_answer individual = pp city_to_search.s individual;
city_to_search_sortal_usr_answer answer = answer;
city_to_search_propositional_usr_answer answer = pp city_to_search.s answer;
city_user_answer answer = answer;
city_individual individual = individual;
weather = pp "weather";
weather_resolve_ynq_2 = resolve_ynq weather;
ask_weather = ask_whq weather;
weather_sys_answer_0 = pp "weather" string_constant_0;
weather_sys_answer_1 = pp "weather" string_constant_1;
weather_sys_answer_2 = pp "weather" string_constant_2;
weather_sys_answer_3 = pp "weather" string_constant_3;
weather_sys_answer_4 = pp "weather" string_constant_4;
weather_sys_answer_5 = pp "weather" string_constant_5;
weather_sys_answer_6 = pp "weather" string_constant_6;
weather_sys_answer_7 = pp "weather" string_constant_7;
weather_sys_answer_8 = pp "weather" string_constant_8;
weather_sys_answer_9 = pp "weather" string_constant_9;
weather_sortal_usr_answer answer = answer;
weather_propositional_usr_answer answer = pp weather.s (ss ("\"" ++ answer.s ++ "\""));
country_to_search = pp "country_to_search";
country_to_search_sys_answer individual = pp country_to_search.s individual;
country_to_search_sortal_usr_answer answer = answer;
country_to_search_propositional_usr_answer answer = pp country_to_search.s answer;
country_user_answer answer = answer;
country_individual individual = individual;
temperature = pp "temperature";
temperature_resolve_ynq_3 = resolve_ynq temperature;
ask_temperature = ask_whq temperature;
temperature_user_question_4 city_to_search country_to_search = ask_whq temperature city_to_search country_to_search;
temperature_sys_answer_0 = pp "temperature" string_constant_0;
temperature_sys_answer_1 = pp "temperature" string_constant_1;
temperature_sys_answer_2 = pp "temperature" string_constant_2;
temperature_sys_answer_3 = pp "temperature" string_constant_3;
temperature_sys_answer_4 = pp "temperature" string_constant_4;
temperature_sys_answer_5 = pp "temperature" string_constant_5;
temperature_sys_answer_6 = pp "temperature" string_constant_6;
temperature_sys_answer_7 = pp "temperature" string_constant_7;
temperature_sys_answer_8 = pp "temperature" string_constant_8;
temperature_sys_answer_9 = pp "temperature" string_constant_9;
temperature_sortal_usr_answer answer = answer;
temperature_propositional_usr_answer answer = pp temperature.s (ss ("\"" ++ answer.s ++ "\""));
unknown_string unknown = ss ("\"" ++ unknown.s ++ "\"");
mkUnknown string = ss string.s;
}
