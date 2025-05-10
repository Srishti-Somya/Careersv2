{ pkgs }: {
  deps = [
    pkgs.python3
    (pkgs.writeShellScriptBin "python" ''
      exec ${pkgs.python3}/bin/python3 "$@"
    '')
  ];
}
