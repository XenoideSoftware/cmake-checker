from conan import ConanFile
import os


class CmakeCheckerConan(ConanFile):
    name = "cmake-checker"
    version = "0.1.0"  # version file (source of truth)
    python_requires = "xenoide-base/0.1.0"
    python_requires_extend = "xenoide-base.XenoideCMake"
    package_type = "application"

    description = "Xenoide CMake style checker"
    license = "MIT"

    exports_sources = "CMakeLists.txt", "src/*", "golden/*", "rules/*"

    def requirements(self):
        self.requires("nlohmann_json/3.12.0")
        self.requires("rapidyaml/0.7.1",
                      options={"with_default_callback_uses_exceptions": True})
        self.requires("cxxopts/3.3.1")
        self.requires("fmt/[>=11 <12]")
        self.requires("chaiscript/6.1.0")

    def package_info(self):
        # Standard pattern for a tool_requires application package.
        self.cpp_info.frameworkdirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
        self.cpp_info.includedirs = []
        self.buildenv_info.prepend_path(
            "PATH", os.path.join(self.package_folder, "bin"))
