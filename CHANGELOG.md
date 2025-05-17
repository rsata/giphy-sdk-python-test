# Changelog

## 0.1.0-alpha.1 (2025-05-17)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/rsata/giphy-sdk-python-test/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** manual updates ([#6](https://github.com/rsata/giphy-sdk-python-test/issues/6)) ([595cb4a](https://github.com/rsata/giphy-sdk-python-test/commit/595cb4a19d6a6c0ef384298847a8b9c576338d23))
* **api:** manual updates ([#7](https://github.com/rsata/giphy-sdk-python-test/issues/7)) ([55e0eec](https://github.com/rsata/giphy-sdk-python-test/commit/55e0eec6210abed7bbccffcba31800000c219c8c))
* **api:** update via SDK Studio ([b8bec18](https://github.com/rsata/giphy-sdk-python-test/commit/b8bec181f87a2f359d90cbc7ff5612713792819d))
* **client:** support digest authentication ([1f9a7e1](https://github.com/rsata/giphy-sdk-python-test/commit/1f9a7e1dbb3300e7475eb23cc9b541f7dcc84864))


### Bug Fixes

* **package:** support direct resource imports ([971ceae](https://github.com/rsata/giphy-sdk-python-test/commit/971ceaef077cf12697b15c758567e3e4e2e174ea))
* **perf:** optimize some hot paths ([e354d9e](https://github.com/rsata/giphy-sdk-python-test/commit/e354d9e6a6c937c71ab6c5e5380f7fefdd3b335e))
* **perf:** skip traversing types for NotGiven values ([febb826](https://github.com/rsata/giphy-sdk-python-test/commit/febb8267c5d2f0f3bb0cf57eca4d35921986e4de))
* pluralize `list` response variables ([#5](https://github.com/rsata/giphy-sdk-python-test/issues/5)) ([37bc1ce](https://github.com/rsata/giphy-sdk-python-test/commit/37bc1ce58884e160add2bd3ef2b41b73fc670536))
* **pydantic v1:** more robust ModelField.annotation check ([70a1e48](https://github.com/rsata/giphy-sdk-python-test/commit/70a1e48e8f452d258a5b422212519ce068d1f171))


### Chores

* broadly detect json family of content-type headers ([4849af6](https://github.com/rsata/giphy-sdk-python-test/commit/4849af6ac7fca047d767f6b94ca943d533bd41f5))
* **ci:** add timeout thresholds for CI jobs ([27adfdf](https://github.com/rsata/giphy-sdk-python-test/commit/27adfdf6de58f8743a4b160c11284e2555e70bf3))
* **ci:** fix installation instructions ([a399fb1](https://github.com/rsata/giphy-sdk-python-test/commit/a399fb19c04185be33a1342ddc270312c59507b7))
* **ci:** only use depot for staging repos ([e3c282b](https://github.com/rsata/giphy-sdk-python-test/commit/e3c282b2c95a0263ba27bd183c908bff6d915292))
* **ci:** upload sdks to package manager ([b8a2a32](https://github.com/rsata/giphy-sdk-python-test/commit/b8a2a326e0bad93173556da9f354838e1db8c273))
* **client:** minor internal fixes ([5fddc65](https://github.com/rsata/giphy-sdk-python-test/commit/5fddc65343d2b81c8629fd91907496df2041d2d2))
* fix typos ([#4](https://github.com/rsata/giphy-sdk-python-test/issues/4)) ([6732fa5](https://github.com/rsata/giphy-sdk-python-test/commit/6732fa5fa8caf69b0c5d2d072fd97d560b85213f))
* go live ([#1](https://github.com/rsata/giphy-sdk-python-test/issues/1)) ([aaf21ad](https://github.com/rsata/giphy-sdk-python-test/commit/aaf21ada749015f9c9968f694d9fb81944653d94))
* **internal:** avoid errors for isinstance checks on proxies ([0cdb8a9](https://github.com/rsata/giphy-sdk-python-test/commit/0cdb8a9c996c6a5097812f60de3f62b67fda914a))
* **internal:** base client updates ([84968bc](https://github.com/rsata/giphy-sdk-python-test/commit/84968bcd8750a98c73c8f1941ac2498f19914ada))
* **internal:** bump pyright version ([3d641af](https://github.com/rsata/giphy-sdk-python-test/commit/3d641af1d1c4d3b955df2c49c629f75de1b6f397))
* **internal:** codegen related update ([ac79e6c](https://github.com/rsata/giphy-sdk-python-test/commit/ac79e6c9050262d8fcd0a2be890b924cab669420))
* **internal:** codegen related update ([107164d](https://github.com/rsata/giphy-sdk-python-test/commit/107164d12a619742f951f171f93f52434ed6d3e6))
* **internal:** expand CI branch coverage ([724d6b8](https://github.com/rsata/giphy-sdk-python-test/commit/724d6b802e5ea07251b8e1f749d18e7ce4ffc6a8))
* **internal:** fix list file params ([965fc49](https://github.com/rsata/giphy-sdk-python-test/commit/965fc49f4316da021863be74dba17ddbc5f1418a))
* **internal:** import reformatting ([e3bf078](https://github.com/rsata/giphy-sdk-python-test/commit/e3bf078d55c1c4c2366322d7bb7bf86a01989163))
* **internal:** reduce CI branch coverage ([26a5c42](https://github.com/rsata/giphy-sdk-python-test/commit/26a5c4281c00256a1ffcb5486a4fe4942df17de8))
* **internal:** refactor retries to not use recursion ([376de56](https://github.com/rsata/giphy-sdk-python-test/commit/376de56494041057ac2ab639f4756eb0ba4dfe3d))
* **internal:** remove trailing character ([#8](https://github.com/rsata/giphy-sdk-python-test/issues/8)) ([367c351](https://github.com/rsata/giphy-sdk-python-test/commit/367c3518a91cc90a28437640b4911f5cacf71b5a))
* **internal:** slight transform perf improvement ([#9](https://github.com/rsata/giphy-sdk-python-test/issues/9)) ([5dae206](https://github.com/rsata/giphy-sdk-python-test/commit/5dae20609e6c15e9951338567687d5aa04277428))
* **internal:** update models test ([aee4f88](https://github.com/rsata/giphy-sdk-python-test/commit/aee4f884ddc79b56d625e4c22c965d32ce4f2a39))
* **internal:** update pyright settings ([3a1991f](https://github.com/rsata/giphy-sdk-python-test/commit/3a1991fea093aa8b63a45aa93c6f24ebd8403469))
* update SDK settings ([#3](https://github.com/rsata/giphy-sdk-python-test/issues/3)) ([34f77a6](https://github.com/rsata/giphy-sdk-python-test/commit/34f77a6c09c673a9093314b0f9bb407594d914a7))
