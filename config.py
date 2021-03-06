# -*- coding: utf-8 -*-"

rebasedb = 'rebase-latest.db'

rebase_baseline_branch = 'chromeos-5.4'
android_baseline_branch = 'android-5.4'

rebase_target = 'latest'

android_site = "https://android.googlesource.com/"
kernel_site = "https://git.kernel.org/"
chromium_site = "https://chromium.googlesource.com/"

# Set to None if unused
android_repo = android_site + "kernel/common"
next_repo = kernel_site + "pub/scm/linux/kernel/git/next/linux-next"
upstream_repo = kernel_site + "pub/scm/linux/kernel/git/torvalds/linux"
stable_repo = kernel_site + "pub/scm/linux/kernel/git/stable/linux-stable"
chromeos_repo = chromium_site + "chromiumos/third_party/kernel"

chromeos_path = "linux-chrome"
upstream_path = "linux-upstream"
stable_path = "linux-stable" if stable_repo else None
android_path = "linux-android" if android_repo else None
next_path = "linux-next" if next_repo else None

# Clear subject_droplist as follows to keep andoid patches
# subject_droplist = []
subject_droplist = ["ANDROID:", "Android:", "android:"]

# List of SHAs to be dropped manually, for example because they are
# upstream but not auto-detected by the tool.
sha_droplist = [
	[ "9ab7893e57cd", "upstream commit 44758bafa536" ],
	[ "5482ed86293b", "upstream commit d30f370d3a49" ],
	[ "80269d1d18e8", "upstream commit 145d59baff59" ],
	[ "64096771a56d", "upstream commit b9b05664ebf6" ],
	[ "eff9d0917462", "upstream commit 93fe48a58590" ],
	[ "b716d03da4f7", "upstream commit f567ff6c76f7" ],
	]

droplist = [('drivers/net/wireless/iwl7000', 'Intel'),
#           ('drivers/gpu/drm/i915', 'Intel'),
#           ('drivers/gpu/drm/amd', 'AMD')
	    ]

topiclist = \
    [["chromeos",
      ["chromeos", "COMMIT-QUEUE.ini", "PRESUBMIT.cfg"]],
     ["cros_ec/iio",
      ["drivers/iio/common/cros_ec_sensors",
       "drivers/iio/accel/cros_ec_accel_legacy.c",
       "drivers/iio/pressure/cros_ec_baro.c",
       "drivers/iio/counter/cros_ec_sensors_sync.c",
       "drivers/iio/light/cros_ec_light_prox.c",
       "include/linux/iio/common/cros_ec_sensors_core.h",
	"Documentation/ABI/testing/sysfs-bus-iio-cros-ec"
       ]],
     ["cros_ec/wilco",
      [ "drivers/platform/chrome/wilco_ec", "drivers/rtc/rtc-wilco-ec",
      "drivers/power/supply/wilco-charger",
      "include/linux/platform_data/wilco-ec.h",
      "Documentation/ABI/testing/debugfs-wilco-ec",
      "Documentation/ABI/testing/sysfs-platform-wilco-ec" ]],
     ["cros_ec/extcon",
      ["drivers/extcon/extcon-usbc-cros_ec",
       "drivers/extcon/extcon-tcss-cros-ec.c",
       "drivers/extcon/extcon-tcss-cros-ec.h",
       "Documentation/devicetree/bindings/extcon/extcon-cros-ec.txt"
      ]],
     ["cros_ec",
      ["drivers/mfd/cros_ec", "drivers/power/cros",
       "drivers/rtc/rtc-cros-ec", "drivers/platform/chrome",
       "drivers/platform/x86/chrome", "drivers/platform/arm/chrome",
       "drivers/input/keyboard/cros_ec",
       "drivers/power/supply/cros_usbpd-charger.c",
       "drivers/pwm/pwm-cros-ec.c",
       "drivers/regulator/cros_ec",
       "drivers/i2c/busses/i2c-cros-ec", "include/linux/mfd/cros_ec",
       "include/linux/chromeos",
       "sound/soc/codecs/cros_ec_codec.c",
       "Documentation/devicetree/bindings/chrome",
       "Documentation/ABI/testing/sysfs-class-chromeos-driver-cros-ec-vbc"
       "Documentation/ABI/testing/debugfs-cros-ec"
       ]],
     ["power",
      ["drivers/power", "drivers/base/power", "kernel/power", "drivers/opp",
       "include/dt-bindings/power", "include/linux/power",
       "include/linux/pm", "Documentation/power", "arch/x86/power",
       "Documentation/devicetree/bindings/power"]],
     ["usb-gadget",
      ["drivers/usb/gadget"]],
     ["usb",
      ["drivers/usb", "include/linux/usb", "include/uapi/linux/usb",
       "Documentation/devicetree/bindings/usb",
       "tools/usb"]],
     ["arm/mali",
      ["drivers/gpu/arm"]],
     ["drm/amd",
      ["drivers/gpu/drm/amd"]],
     ["drm/i915",
      ["drivers/gpu/drm/i915"]],
     ["drm/mediatek",
      ["drivers/gpu/drm/mediatek"]],
     ["drm/qualcomm",
      ["drivers/gpu/drm/msm"]],
     ["drm/panel",
      ["drivers/gpu/drm/panel"]],
     ["drm/rockchip",
      ["drivers/gpu/drm/rockchip"]],
     ["drm/virtio",
      ["drivers/gpu/drm/virtio", "include/drm/virtio_drm.h", "include/uapi/drm/virtgpu_drm.h" ]],
     ["gpu/other",
      ["drm", "drivers/gpu", "include/drm", "Documentation/devicetree/bindings/drm",
       "include/uapi/drm"]],
     ["media",
      ["drivers/media", "drivers/staging/media",
       "include/media", "include/uapi/linux/videodev2.h",
       "include/uapi/linux/v4l2-controls.h", "Documentation/media" ]],
     ["video",
      ["drivers/video"]],
     ["input",
      ["drivers/input", "include/linux/input"]],
     ["iio",
      ["drivers/iio", "drivers/staging/iio", "Documentation/driver-api/iio",
       "Documentation/devicetree/bindings/iio",
       "Documentation/devicetree/bindings/staging/iio",
       "Documentation/iio", "include/linux/iio", "include/uapi/linux/iio",
       "include/dt-bindings/iio"]],
     ["mmc",
      ["drivers/mmc", "Documentation/mmc", "include/linux/mmc",
       "include/uapi/linux/mmc"]],
     ["mtd",
      ["drivers/mtd", "include/linux/mtd", "include/uapi/mtd",
       "Documentation/mtd", "Documentation/devicetree/bindings/mtd"]],
     ["bluetooth",
      ["net/bluetooth", "drivers/bluetooth",
       "Documentation/devicetree/bindings/net/btusb.txt",
       "include/net/bluetooth"]],
     ["wireless",
      ["net/wireless", "drivers/net/wireless",
       "include/uapi/linux/wireless.h",
       "Documentation/devicetree/bindings/net/wireless"]],
     ["net",
      ["drivers/net/usb", "net", "drivers/net", "include/linux/tcp.h",
       "include/uapi/linux/tcp.h",
       "include/net", "include/dt-bindings/net", "include/linux/net",
       "include/uapi/linux/sockios.h"]],
     ["sound/intel",
      ["sound/soc/intel", "sound/soc/sof/intel"]],
     ["sound/mediatek",
      ["sound/soc/mediatek"]],
     ["sound/rockchip",
      ["sound/soc/rockchip"]],
     ["sound/other",
      ["sound", "Documentation/devicetree/bindings/sound", "include/sound",
       "include/uapi/sound"]],
     ["security",
      ["security", "include/linux/alt-syscall.h", "include/linux/syscalls.h",
       "arch/arm64/kernel/alt-syscall.c",
       "arch/x86/kernel/alt-syscall.c", "kernel/alt-syscall.ch"]],
     ["android",
      ["android", "Documentation/android", "drivers/android",
       "drivers/staging/android",
       "include/linux/android", "include/uapi/linux/android"]],
     ["fs/pstore",
      ["fs/pstore", "include/linux/pstore",
       "Documentation/devicetree/bindings/reserved-memory/ramoops.txt",
       "Documentation/devicetree/bindings/misc/ramoops.txt",
       "Documentation/ramoops.txt"]],
     ["fs/ecryptfs",
      ["fs/ecryptfs"]],
     ["fs/esdfs",
      ["fs/esdfs"]],
     ["fs/other",
      ["fs"]],
     ["hid",
      ["drivers/hid"]],
     ["md",
      ["drivers/md", "init/do_mounts_dm.c", "Documentation/device-mapper/boot.txt"]],
     ["thermal",
      ["drivers/thermal", "include/linux/thermal",
       "Documentation/devicetree/bindings/thermal"]],
     ["regulator",
      ["Documentation/devicetree/bindings/regulator", "drivers/regulator",
      "include/linux/regulator"]],
     ["scsi",
      ["drivers/scsi"]],
     ["virtio",
      ["drivers/virtio", "include/uapi/linux/virtwl.h"]],
     ["sysrq",
      ["drivers/tty/sysrq.c"]],
     ["firmware/google",
      ["drivers/firmware/google"]],
     ["tpm",
      ["drivers/char/tpm", "Documentation/devicetree/bindings/security/tpm"]],
     ["lowmem",
      ["include/linux/low-mem-notify.h", "mm/low-mem-notify.c",
       "tools/mm/low-mem-test.c", "drivers/char/mem.c"]],
     ["mm",
      ["mm", "include/linux/mm_metrics.h", "include/linux/swapops.h"]],
     ["scheduler",
      ["include/linux/sched", "kernel/sched"]],
     ["cgroup",
      ["kernel/cgroup"]],
     ["dts/qcom",
      ["arch/arm64/boot/dts/qcom"]],
     ["dts/mediatek",
      ["arch/arm64/boot/dts/mediatek",
       "Documentation/devicetree/bindings/display/mediatek",
       "Documentation/devicetree/bindings/soc/mediatek",
       "Documentation/devicetree/bindings/arm/mediatek"
      ]],
     ["dts/rk3399",
      ["arch/arm64/boot/dts/rockchip"]],
     ["dts/arm",
      ["arch/arm/boot/dts"]],
     ["acpi",
      ["drivers/acpi"]],
     ["container",
      ["arch/arm64/configs/chromiumos-container-vm-arm64_defconfig",
       "arch/x86/configs/chromiumos-container-vm-x86_64_defconfig",
       "arch/x86/configs/x86_64_arcvm_defconfig"]],
     ["drivers/mediatek",
      ["drivers/clk/mediatek",
       "drivers/pinctrl/mediatek",
       "drivers/soc/mediatek"
      ]],
     ["drivers/rockchip",
      ["drivers/clk/rockchip",
       "drivers/soc/rockchip",
       "drivers/crypto/rockchip",
       "drivers/clk/rockchip"
      ]],
     ["cpufreq",
      ["drivers/cpufreq"]],
     ["devfreq",
      ["drivers/devfreq"]],
     ["iommu",
      ["drivers/iommu"]],
     ["remoteproc",
      ["drivers/remoteproc", "drivers/rpmsg", "include/linux/rpmsg" ]],
     ["mfd",
      ["drivers/mfd"]],
     ["arch/arm64",
      ["arch/arm64"]],
     ["arch/arm",
      ["arch/arm"]],
     ["arch/x86",
      ["arch/x86", "drivers/platform/x86"]],
     ["devicetree",
      ["Documentation/devicetree"]],
    ]
