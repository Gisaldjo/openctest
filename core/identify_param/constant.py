import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CUR_DIR, "app")

CTEST_HADOOP_DIR = os.path.join(APP_DIR, "ctest-hadoop")
CTEST_HBASE_DIR = os.path.join(APP_DIR, "ctest-hbase")
CTEST_ZOOKEEPER_DIR = os.path.join(APP_DIR, "ctest-zookeeper")
CTEST_ALLUXIO_DIR = os.path.join(APP_DIR, "ctest-alluxio")
CTEST_FLINK_DIR = os.path.join(APP_DIR, "ctest-flink")
CTEST_FLINK_CLIENTS_DIR = os.path.join(APP_DIR, "ctest-flink-clients")
CTEST_FLINK_KUBERNETES_DIR = os.path.join(APP_DIR, "ctest-flink-kubernetes")
CTEST_FLINK_SCALA_SHELL_DIR = os.path.join(APP_DIR, "ctest-flink-scala-shell")

MODULE_PATH = {
    "hadoop-common": CTEST_HADOOP_DIR,
    "hadoop-hdfs": CTEST_HADOOP_DIR,
    "hbase-server": CTEST_HBASE_DIR,
    "alluxio-core": CTEST_ALLUXIO_DIR,
    "flink-core": CTEST_FLINK_DIR,
    "flink-clients": CTEST_FLINK_CLIENTS_DIR,
    "flink-kubernetes": CTEST_FLINK_KUBERNETES_DIR,
    "flink-scala-shell": CTEST_FLINK_SCALA_SHELL_DIR
}

SRC_SUBDIR = {
    "hadoop-common": "hadoop-common-project/hadoop-common",
    "hadoop-hdfs": "hadoop-hdfs-project/hadoop-hdfs",
    "hbase-server": "hbase-server",
    "zookeeper-server": "zookeeper-server",
    "alluxio-core": "core",
    "flink-core": "flink-core",
    "flink-clients": "flink-clients",
    "flink-kubernetes": "flink-kubernetes",
    "flink-scala-shell": "flink-scala-shell"
}

MVN_TEST_PATH = {
    "hadoop-common": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"]),
    "hadoop-hdfs": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"]),
    "hbase-server": os.path.join(CTEST_HBASE_DIR, SRC_SUBDIR["hbase-server"]),
    "zookeeper-server": os.path.join(CTEST_ZOOKEEPER_DIR, SRC_SUBDIR["zookeeper-server"]),
    "alluxio-core": os.path.join(CTEST_ALLUXIO_DIR, SRC_SUBDIR["alluxio-core"]),
    "flink-core": os.path.join(CTEST_FLINK_DIR, SRC_SUBDIR["flink-core"]),
    "flink-clients": os.path.join(CTEST_FLINK_CLIENTS_DIR, SRC_SUBDIR["flink-clients"]),
    "flink-kubernetes": os.path.join(CTEST_FLINK_KUBERNETES_DIR, SRC_SUBDIR["flink-kubernetes"]),
    "flink-scala-shell": os.path.join(CTEST_FLINK_SCALA_SHELL_DIR, SRC_SUBDIR["flink-scala-shell"])
}

LOCAL_CONF_PATH = {
    "hadoop-common": "results/hadoop-common/conf_params.txt",
    "hadoop-hdfs": "results/hadoop-hdfs/conf_params.txt",
    "hbase-server": "results/hbase-server/conf_params.txt",
    "zookeeper-server": "results/zookeeper-server/conf_params.txt",
    "alluxio-core": "results/alluxio-core/conf_params.txt",
    "flink-core": "results/flink-core/conf_params.txt",
    "flink-clients": "results/flink-clients/conf_params.txt",
    "flink-kubernetes": "results/flink-kubernetes/conf_params.txt",
    "flink-scala-shell": "results/flink-scala-shell/conf_params.txt"
}

SUREFIRE_SUBDIR = "target/surefire-reports/*"

CTEST_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"], SUREFIRE_SUBDIR)
    ],
    "hadoop-hdfs": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"], SUREFIRE_SUBDIR)
    ],
    "hbase-server": [
        os.path.join(CTEST_HBASE_DIR, "hbase-server", SUREFIRE_SUBDIR)
    ],
    "zookeeper-server": [
        os.path.join(CTEST_ZOOKEEPER_DIR, "zookeeper-server", SUREFIRE_SUBDIR)
    ],
    "alluxio-core": [
        os.path.join(CTEST_ALLUXIO_DIR, "core/base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/fs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/hdfs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/proxy", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/worker", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/master", SUREFIRE_SUBDIR)
    ],
    "flink-core": [
        os.path.join(CTEST_FLINK_DIR, "flink-core", SUREFIRE_SUBDIR)
    ],
    "flink-clients": [
        os.path.join(CTEST_FLINK_CLIENTS_DIR, "flink-clients", SUREFIRE_SUBDIR)
    ],
    "flink-kubernetes": [
        os.path.join(CTEST_FLINK_KUBERNETES_DIR, "flink-kubernetes", SUREFIRE_SUBDIR)
    ],
    "flink-scala-shell": [
        os.path.join(CTEST_FLINK_SCALA_SHELL_DIR, "flink-scala-shell", SUREFIRE_SUBDIR)
    ]
}

LOCAL_SUREFIRE_SUFFIX = "surefire-reports/*"

LOCAL_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join("surefire-reports/common/hadoop-common", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-hdfs": [
        os.path.join("surefire-reports/hdfs/hadoop-hdfs", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hbase-server": [
        os.path.join("surefire-reports/hbase/hbase-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "zookeeper-server": [
        os.path.join("surefire-reports/zk/zookeeper-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "alluxio-core": [
        os.path.join("surefire-reports/alluxio-core", LOCAL_SUREFIRE_SUFFIX)
    ],
    "flink-core": [
        os.path.join("surefire-reports/flink-core", LOCAL_SUREFIRE_SUFFIX)
    ],
    "flink-clients": [
        os.path.join("surefire-reports/flink-clients", LOCAL_SUREFIRE_SUFFIX)
    ],
    "flink-kubernetes": [
        os.path.join("surefire-reports/flink-kubernetes", LOCAL_SUREFIRE_SUFFIX)
    ],
    "flink-scala-shell": [
        os.path.join("surefire-reports/flink-scala-shell", LOCAL_SUREFIRE_SUFFIX)
    ]
}
