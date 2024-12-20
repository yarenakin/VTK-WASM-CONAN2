from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
import os

class VtkWasmConan(ConanFile):
    name = "vtk-wasm"
    version = "9.4.0"  # VTK'nin sürümü
    license = "BSD-3-Clause"
    url = "https://vtk.org"
    description = "VTK for WebAssembly with Emscripten"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def source(self):
        target_dir = os.path.join(self.source_folder, "vtk-9.4.0")
        self.output.info(f"Cloning VTK repository into {target_dir}")
        self.run(f"git clone https://gitlab.kitware.com/vtk/vtk.git --branch v9.4.0 {target_dir}")

    def generate(self):
        tc = CMakeToolchain(self)
        
        tc.generator = "Ninja"  # Ninja'yı açıkça belirt
        # Diğer CMake değişkenleri
        tc.variables["BUILD_SHARED_LIBS"] = "OFF"
        tc.variables["CMAKE_BUILD_TYPE"] = "Release"
        tc.variables["VTK_ENABLE_LOGGING"] = "OFF"
        tc.variables["VTK_ENABLE_WRAPPING"] = "OFF"
        tc.variables["VTK_MODULE_ENABLE_VTK_libproj"] = "NO"
        tc.variables["VTK_MODULE_ENABLE_VTK_RenderingLICOpenGL2"] = "DONT_WANT"
        tc.variables["VTK_BUILD_TESTING"] = "OFF"
        tc.variables["VTK_USE_PROJ"] = "OFF"
        tc.variables["VTK_MODULE_ENABLE_VTK_IOHDF5"] = "NO"
        tc.variables["VTK_MODULE_ENABLE_VTK_hdf5"] = "NO"
        tc.variables["VTK_MODULE_ENABLE_VTK_netcdf"] = "NO"
        tc.variables["VTK_SMP_IMPLEMENTATION_TYPE"] = "Sequential"
        tc.variables["VTK_NO_TEST_BIG_ENDIAN"] = "ON"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        source_dir = os.path.join(self.source_folder, "vtk-9.4.0")  # VTK'nin indirildiği alt dizin
        build_dir = os.path.join(self.build_folder, "Release")
        cmake.configure(variables={
            "CMAKE_INSTALL_PREFIX": os.path.join(self.source_folder, "install").replace("\\", "/"),  # Kurulum dizini burada belirttim çünkü conan nedense generate fonk belirtilen dizini görmüyor
            "CMAKE_TOOLCHAIN_FILE": os.path.join(build_dir, "generators", "conan_toolchain.cmake"), 
            "CMAKE_BUILD_TYPE": "Release"
        }, build_script_folder=source_dir)
        cmake.build()
        # cmake.install() yerine manuel ninja install çalıştır
        self.run("ninja install", cwd=self.build_folder)
