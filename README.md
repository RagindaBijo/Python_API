# Python_API

openweathermap.com-იდან აღებული იქნა API,რომელიც აჩვენებს მითითებული ქალაქის ამინდს.API საჭიროებს ქალაქის სახელს, ქვეყნის ISO კოდს და ასევე API KEY-ს.cnt გრაფაში შეტანილი რიცხვი (1-40) გვიჩვენებს შესაბამის დროის მონაკვეთში მოსალოდნელ ამინდს.(საათიების სისტემა openweathermap-ზე დაყოფილია 3-3 საათად.ყოველ ჯერზე cnt-ს 1-ით გაზრდისას პროგრამა გვიჩვენებს 3 საათის შემდეგ მოსალოდნელ ამინდს. 40*3=120, 120/24=5. შესაბამისად პროგრამას შეუძლია გვიჩვენოს მაქსიმუმ 5 დღის ამინდი. თუმცა დროის გრაფები არის ფიქსირებული.ანუ თუ პროგრამის გაშვებისას დრო არის 13:30 , პროგრამა აჩვენებს 12:00 დროის ამინდს, რადგან იგი ფიქსირებულია კონკრეტულ საათებზე. 
დავალების პირველ ნაწილში გამოთანილია მცირე ფუნქციები როგორიცაა 
response code, status code და ასე შემდეგ. JSON ფაილი გადაყვანილია dict ფაილად და შემდეგ Dump-ით არის სტრუქტურულად დალაგებული რის შემდეგაც შენახულია Json ფაილში.

დავალების მეორე ნაწილში გამოტანილია კონკრეტული ინფორმაციები რომელიც ჩვენ გვსურს რომ დავინახოთ.შემდეგ ეს ინფორმაციები ატვირთული არის მონაცემთა ბაზის სახით. საბოლოოდ windows notification-ის გამოყენებით ეს
გამოტანილი ინფორმაცია ვარდება notification-ის სახით როცა პროგრამას გავუშვებთ 
