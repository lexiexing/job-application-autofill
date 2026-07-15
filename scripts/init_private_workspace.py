#!/usr/bin/env python3
"""初始化网申 skill 的私有材料目录，不读取或上传任何文件。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


MATERIAL_FOLDERS = {
    "简历": "resume",
    "成绩单": "transcripts",
    "证书": "certificates",
    "作品集": "portfolio",
    "其他材料": "other",
}


def initialize(skill_dir: Path) -> tuple[Path, list[Path]]:
    skill_dir = skill_dir.expanduser().resolve()
    template = skill_dir / "references" / "profile-template.md"
    if not template.is_file():
        raise FileNotFoundError(f"找不到个人档案模板：{template}")

    private_dir = skill_dir / "private"
    materials_dir = private_dir / "materials"
    created: list[Path] = []

    for folder in MATERIAL_FOLDERS.values():
        path = materials_dir / folder
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(path)

    profile = private_dir / "profile.md"
    if not profile.exists():
        shutil.copyfile(template, profile)
        created.append(profile)

    return profile, created


def main() -> int:
    parser = argparse.ArgumentParser(description="初始化网申 skill 的私有资料空间")
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="skill 根目录；默认自动根据脚本位置确定",
    )
    args = parser.parse_args()

    profile, created = initialize(args.skill_dir)
    print("私人资料空间已就绪。")
    if created:
        print("本次创建：")
        for path in created:
            print(f"- {path}")
    else:
        print("目录已经存在，没有覆盖任何文件。")

    print("\n请直接上传以下材料，Codex 会自动归档：")
    for label, folder in MATERIAL_FOLDERS.items():
        print(f"- {label} → {profile.parent / 'materials' / folder}")
    print(f"- 自动生成的个人档案 → {profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
