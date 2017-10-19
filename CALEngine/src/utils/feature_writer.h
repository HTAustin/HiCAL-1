#ifndef FEATURE_WRITER_H
#define FEATURE_WRITER_H

#include "../sofiaml/sf-sparse-vector.h"
#include <fstream>
#include <memory>

namespace CAL{
    namespace utils{
        class FeatureWriter{
            protected:
                static const char DELIM_CHAR = '\n';
                FILE *fp;
            public:
                FeatureWriter(const string &fname){ fp = fopen(fname.c_str(), "wb"); setvbuf(fp, nullptr, _IOFBF, 1 << 25); }
                virtual void write(const std::unique_ptr<SfSparseVector> &spv) = 0;
                ~FeatureWriter(){fclose(fp);}
        };

        class BinFeatureWriter:public FeatureWriter {
            uint32_t num_records = 0;
            public:
                BinFeatureWriter(const string &file_name);
                void write(const std::unique_ptr<SfSparseVector> &spv) override;
                // Write final headers
                void finish();
        };

        class SVMlightFeatureWriter:public FeatureWriter {
            public:
                SVMlightFeatureWriter(const string &file_name);
                void write(const std::unique_ptr<SfSparseVector> &spv) override;
        };
    }
}
#endif // FEATURE_WRITER_H
