VTK WebAssembly (Conan2 ve Emscripten ile)
Bu proje, Visualization Toolkit (VTK) kütüphanesini WebAssembly platformunda çalıştırmak için gerekli olan altyapıyı sağlar. Projeniz için bağımlılıkları kurmak ve derlemeyi kolaylaştırmak amacıyla bir run.bat dosyası eklenmiştir.

Nasıl Çalıştırılır?
Depoyu Klonlayın

``` bash
git clone https://github.com/yarenakin/VTK-WASM-CONAN2.git
cd VTK-WASM-CONAN2
```
run.bat Dosyasını Çalıştırın
Windows üzerinde run.bat dosyasını çalıştırarak gerekli adımları otomatik olarak tamamlayabilirsiniz.

```bash
./run.bat
```

Projeyi Kullanmak:
Ortam değişkenlerinden VTK_CONAN_DIR ayarlanmıştır. Bu değişkeni kendi CMakeLists.txt dosyanızda kullanabilirsiniz:

```cmake
set(VTK_DIR $ENV{VTK_CONAN_DIR})
find_package(VTK REQUIRED)
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------VTK WebAssembly (with Conan2 and Emscripten)
This project provides the necessary setup to build and run the Visualization Toolkit (VTK) library on the WebAssembly platform. A run.bat script is included to simplify dependency installation and build steps.

How to Run?
Clone the Repository
``` bash
git clone https://github.com/yarenakin/VTK-WASM-CONAN2.git
cd VTK-WASM-CONAN2
```

Run the run.bat Script
On Windows, simply run the run.bat file to automatically complete all required
```bash
./run.bat
```
Using the Project
The VTK_CONAN_DIR environment variable is set during the process. You can use this in your CMakeLists.txt file:

```cmake
set(VTK_DIR $ENV{VTK_CONAN_DIR})
find_package(VTK REQUIRED)
```
