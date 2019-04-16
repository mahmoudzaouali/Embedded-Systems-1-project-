# Almunther Alawadhi         /         Mahmoud Chick Zaouali
# Embedded-Systems-vize-projesi-

Youtube Link : 
https://www.youtube.com/watch?v=4VVAKa7HvEk&feature=youtu.be

Bu porjede QR kodu generator ve çözücü ile güvenli systemi tasarladık. rasbperry pi B model, webcamer, servomotor, buzzer ve tasaraladığımız Login Acount interface ile bu projeyi inşa edilmiştir. bir kurumun dışından gelen kişilere o kuruma geriş ve çıkışlaranı güvenli, kolay, ucuz ve takip edilebilecek bir system amacıyla bu projeyi yaptık. bu projede arayüzü ve database yapısı (structure) tasarlamak, data akışı, görüntü işlemesi ve IoT'sini ve donanım parçaları sürmesi Rasbperry Pi ve Python3 programı kullandık. 
bir korumun dışından gelenlare giriş sağlamak için o kurumun hesapında oyelik sahıp olanlarından birisi o hesap üzerinden giriş SecretWord ve misafirin emailini girirerek onaylandığınde o SecretWord 128 bitlik şifre formunda şifrelenip QR kod şeklinde misafirin emailine gönderilecek.o şifre sadece bir defa kullanılır yanında o şifre kim oluşturdu ve kime oluşturulduğunu kayıttadır. 
Misafir o QR kodu emilindan alıp kurumun kapısındaki giriş kamerasına göstererek kapıyı açılacak QR kodu doğru ise, yalnış ise uyarı alarm çalışacaktır.
Note: Login Account database bilgisarda olacak ama QR kodu ve misafirla ilgili bilgiler internettedir.
