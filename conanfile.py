from conans import ConanFile, CMake, tools

class OpenarincConan(ConanFile):
    name = "openarinc"
    version = "1.0"
    license = "Apache 2.0"
    author = "Manuel Freiholz (https://mfreiholz.de)"
    url = "https://github.com/insaneFactory/conan-openarinc"
    description = "Library to parse A429"
    topics = ("arinc", "a429")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    build_requires = (
        "cmake_installer/3.12.1@conan/stable"
    )

    def configure(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/stewbond/openarinc.git")
        #self.run("cd aisparser && git fetch --all --tags --prune && git checkout tags/v" + self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="openarinc/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["openarinc"]
