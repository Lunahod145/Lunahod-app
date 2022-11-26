{
    description = "Lunohod";
    inputs = {
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = {self, nixpkgs, flake-utils}:
        flake-utils.lib.eachDefaultSystem(system:
            let
                pkgs = nixpkgs.legacyPackages.${system};
            in {
                devShells.default = pkgs.mkShell rec {
                    buildInputs = with pkgs; [
                        qt6.full
                        stdenv.cc.cc.lib
                        qt6.qtmultimedia
                        glibc
                    ];

                    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath buildInputs;
                    PATH = "${pkgs.qt6.full}/bin";
                    QT_PLUGIN_PATH = "${pkgs.qt6.full}/lib/qt-6/plugins";

                    shellHook = ''
                        echo ${pkgs.qt6.qtmultimedia}
                        function patch_(){
                            patchelf --set-interpreter ${pkgs.glibc}/lib/ld-linux-x86-64.so.2 $1
                        }
                        export -f patch_
                    '';
                };
            }
        );
}
