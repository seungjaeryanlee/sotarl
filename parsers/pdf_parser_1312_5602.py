import camelot

from pdf_parser import PDFParser


class PDFParser_1312_5602(PDFParser):
    def _format_df(self):
        tables = camelot.read_pdf("../pdfs/1312.5602.pdf", pages="8", flavor="lattice")
        df_noop = tables[0].df
        df_noop = self._remove_index_and_header(df_noop)
        df_noop = self._standardize_env_names(df_noop)
        df_noop = self._standardize_scores(df_noop)
        # TODO(seungjaeryanlee): Assumed they used NOOP start... but there is no mention in the paper
        df_noop = df_noop.add_suffix("_noop")

        self.df = df_noop

        # Remove citation marks
        self.df.rename(index={
            "Sarsa [3]": "Sarsa",
            "Contingency [4]": "Contingency",
        }, inplace=True)

        self._add_paper_metadata(
            title="Playing Atari with Deep Reinforcement Learning",
            authors="Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, Martin Riedmiller",
            link="https://arxiv.org/abs/1312.5602",
            arxiv_id="1312.5602",
            arxiv_version=1,
            bibtex="""
            @article{DBLP:journals/corr/MnihKSGAWR13,
                author    = {Volodymyr Mnih and
                            Koray Kavukcuoglu and
                            David Silver and
                            Alex Graves and
                            Ioannis Antonoglou and
                            Daan Wierstra and
                            Martin A. Riedmiller},
                title     = {Playing Atari with Deep Reinforcement Learning},
                journal   = {CoRR},
                volume    = {abs/1312.5602},
                year      = {2013},
                url       = {http://arxiv.org/abs/1312.5602},
                archivePrefix = {arXiv},
                eprint    = {1312.5602},
                timestamp = {Mon, 13 Aug 2018 16:47:42 +0200},
                biburl    = {https://dblp.org/rec/bib/journals/corr/MnihKSGAWR13},
                bibsource = {dblp computer science bibliography, https://dblp.org}
            }""",
        )
        self._pre_add_agent_metadata()
        self._add_agent_metadata("Random", fullname="Random", nickname="Random")
        self._add_agent_metadata("Sarsa", fullname="Sarsa", nickname="Sarsa")
        self._add_agent_metadata("Contingency", fullname="Contingency", nickname="Contingency")
        self._add_agent_metadata("DQN", fullname="Deep Q-Network", nickname="DQN")
        self._add_agent_metadata("Human", fullname="Human", nickname="Human")


if __name__ == "__main__":
    parser = PDFParser_1312_5602()
    print(parser.df)
