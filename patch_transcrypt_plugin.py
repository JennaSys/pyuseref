import os
import patch


is_windows = os.name == 'nt'

posix_patch = b"""
--- asset.js	2020-11-30 17:49:49.690000000 -0800
+++ asset.js	2020-11-30 17:50:42.795302864 -0800
@@ -1,5 +1,5 @@
 const Asset = require('parcel-bundler/src/Asset');
-const logger = require('parcel-bundler/src/Logger');
+const logger = require('@parcel/logger/src/Logger');
 const child_process = require('child_process');
 const path = require('path');
 const fs = require('fs');
 """

win_patch = b"""
--- asset.js	2020-11-30 17:49:49.690000000 -0800
+++ asset.js	2020-11-30 17:50:42.795302864 -0800
@@ -1,5 +1,5 @@
 const Asset = require('parcel-bundler/src/Asset');
-const logger = require('parcel-bundler/src/Logger');
+const logger = require('@parcel/logger/src/Logger');
 const child_process = require('child_process');
 const path = require('path');
 const fs = require('fs');
@@ -11,7 +11,7 @@
 // package.json, then modify as needed.
 const DEFAULT_PACKAGE_CONFIG = {
     "parcel-plugin-python": {
-        "command": "python3 -m transcrypt",
+        "command": "python -m transcrypt",
         "arguments": [
             /*  note that --build should normally not be used because multiple .py entry points         */
             /*  cause transcrypt to delete the first run's __target__ as it starts the second call.     */
@@ -140,7 +140,7 @@
         //    (  _ _)/ /-." ~~
         //     `( )_ )/
         //      <_  <_
-        this.content = `export * from "${this.importPath}";`;
+        this.content = `export * from "${this.importPath.replace(/\\/g, '/')}";`;

         // return the transpiled result
         return this.content;
"""


def main():
    print('Patching Transcrypt Parcel Plugin...')
    patch_data = win_patch if is_windows else posix_patch

    try:
        patch_set = patch.fromstring(patch_data)
        patch_set.apply(root=os.path.join('.', 'node_modules', 'parcel-plugin-transcrypt'))
        print("Transcrypt Parcel Plugin patch completed!")
    except Exception as e:
        print("Transcrypt Parcel Plugin patch failed!")
        print(e)


if __name__ == '__main__':
    main()
