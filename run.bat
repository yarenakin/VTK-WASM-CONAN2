@echo off

REM Projenin bulunduğu dizini al ve ters eğik çizgileri ileri eğik çizgilere çevir
set PROJECT_DIR=%cd%
set PROJECT_DIR_X=%PROJECT_DIR:\=/%

REM VTK'nin kurulu olup olmadığını kontrol edin
if exist "%PROJECT_DIR_X%/vtk-9.4.0" (
    echo VTK zaten indirilmis, bu adimi atliyoruz.
) else (
    REM Projenin kaynak kodlarını indirin
    conan source .
    if %errorlevel% neq 0 (
        echo Kaynak kodlar indirilirken bir hata oluştu.
        exit /b %errorlevel%
    )
)
pause

REM Conan ile bağımlılıkları yükle ve toolchain oluştur bu vtkyı ve emsdkyı indirme adımı aslında
conan install . --profile:host=emscripten_profile --profile:build=default --build=missing
if %errorlevel% neq 0 (
    echo Conan bağimliliklari yüklerken bir hata oluştu.
    exit /b %errorlevel%
)
pause

cd build
if %errorlevel% neq 0 (
    echo Build dizinine geçerken bir hata oluştu.
    exit /b %errorlevel%
)
pause

REM cmake -G "Ninja" -DCMAKE_TOOLCHAIN_FILE=Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release %PROJECT_DIR_X%/vtk-9.4.0 bunun ile aynı işi yapar
REM ninja ve ninja install çalıştırır derleme ve kurulumu yapar
conan build ..
if %errorlevel% neq 0 (
    echo CMake yapilandirilmasi sirasinda bir hata oluştu.
    exit /b %errorlevel%
)
pause

 
REM Kurulum dizinini ortam değişkenine ekle
setx  VTK_CONAN_DIR "%PROJECT_DIR%\install\lib\cmake\vtk-9.4" 
if %errorlevel% neq 0 (
    echo Ortam değişkeni ayarlanirken bir hata oluştu.
    exit /b %errorlevel%
)
pause

REM İşlem tamamlandı
echo İşlem tamamlandi. Derleme, kurulum ve VTK_CONAN_DIR ortam değişkeni ayarlandi.
